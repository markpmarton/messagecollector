import pytest
from uuid import uuid4
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from config import DB_CONN_STR

existing_user_id: str = None
existing_type_id: str = None

@pytest.fixture(autouse=True)
def pre_post_actions():
    from models import User, Message, Type

    try:
        print(DB_CONN_STR)
        engine = create_engine(DB_CONN_STR)
        test_user = User(customerid=1, name="Test User")
        test_type = Type(name="Test Type")

        existing_user_id = test_user.uuid
        existing_type_id = test_type.uuid

        test_message = Message(
            uuid=f"{uuid4()}",
            app_user_id=test_user.uuid,
            type_id=test_type.uuid,
            amount="1.11"
        )
        with Session(engine) as session:
            session.add_all([test_user, test_type, test_message])
            session.commit()

        yield

        with Session(engine) as session:
            session.delete(test_message)
            session.delete(test_user)
            session.delete(test_type)
            session.commit()
    except Exception as e:
        print(str(e))

def test_saving_message_with_good_input_and_existing_type_and_user():
    from models import Message
    from repository import MessageRepository
    
    msg_repository = MessageRepository()
    message = Message(
        uuid=f"{uuid4()}",
        app_user_id=existing_user_id,
        type_id=existing_type_id,
        amount="0.12"
    )
    assert msg_repository.store_message(message)

def test_saving_message_with_good_input_and_missing_user_and_type():
    from models import Message
    from repository import MessageRepository
    
    msg_repository = MessageRepository()
    message = Message(
        uuid=f"{uuid4()}",
        app_user_id=f"{uuid4()}",
        type_id=f"{uuid4()}",
        amount="0.12"
    )
    assert not msg_repository.store_message(message)

def test_api_collect_message_with_good_input_and_existing_type_and_user():
    from fastapi.testclient import TestClient
    from main import app
    from dto_models import CollectMessageDto

    client = TestClient(app)
    response = client.post(
        "/message/collect",
        json={
            "uuid": f"{uuid4()}",
            "customerId": 1,
            "type": "Test Type",
            "amount": "0.13"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_api_collect_message_with_good_input_and_existing_type_but_missing_user():
    from models import User
    from fastapi.testclient import TestClient
    from main import app
    from dto_models import CollectMessageDto

    client = TestClient(app)
    response = client.post(
        "/message/collect",
        json={
            "uuid": f"{uuid4()}",
            "customerId": 999,
            "type": "Test Type",
            "amount": "0.13"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

    with Session(create_engine(DB_CONN_STR)) as session:
        user = session.query(User).filter_by(customerid=999).first()
        session.delete(user)
        session.commit()
        

def test_api_collect_message_with_good_input_and_existing_type_but_missing_user():
    from models import Type
    from fastapi.testclient import TestClient
    from main import app
    from dto_models import CollectMessageDto

    client = TestClient(app)
    response = client.post(
        "/message/collect",
        json={
            "uuid": f"{uuid4()}",
            "customerId": 1,
            "type": "Non Existing Type",
            "amount": "0.13"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

    with Session(create_engine(DB_CONN_STR)) as session:
        act_type = session.query(Type).filter_by(name="Non Existing Type").first()
        session.delete(act_type)
        session.commit()


def test_api_collect_message_with_good_input_and_existing_type_but_missing_user():
    from models import Type, User
    from fastapi.testclient import TestClient
    from main import app
    from dto_models import CollectMessageDto

    client = TestClient(app)
    response = client.post(
        "/message/collect",
        json={
            "uuid": f"{uuid4()}",
            "customerId": 999,
            "type": "Non Existing Type",
            "amount": "0.13"
        }
    )
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

    with Session(create_engine(DB_CONN_STR)) as session:
        user = session.query(User).filter_by(customerid=999).first()
        act_type = session.query(Type).filter_by(name="Non Existing Type").first()
        session.delete(act_type)
        session.delete(user)
        session.commit()