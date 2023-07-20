from uuid import uuid4
import pytest
import os
import psycopg2

from logger import Logger


@pytest.fixture(scope="session", autouse=True)
def run_pre_post():
    yield

    conn = psycopg2.connect(
        host=os.environ["DB_CONTAINER_NAME"],
        port=os.environ["DB_PORT"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
    )
    query = ""
    cur = conn.cursor()

    with open("/tools/clear_db.sql", "r") as reader:
        query = reader.read()
    cur.execute(query)
    conn.commit()


def test_api_collect_message_with_good_input_existing_type_and_user():
    from fastapi.testclient import TestClient
    from main import app

    client = TestClient(app)
    response = client.post(
        "/message/collect",
        json={
            "uuid": f"{uuid4()}",
            "customerId": 1,
            "type": "Test Type",
            "amount": "0.13",
        },
    )
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_api_collect_message_with_good_input_existing_type_but_missing_user():
    from fastapi.testclient import TestClient
    from main import app

    client = TestClient(app)
    response = client.post(
        "/message/collect",
        json={
            "uuid": f"{uuid4()}",
            "customerId": 999,
            "type": "Test Type",
            "amount": "0.13",
        },
    )
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_api_collect_message_with_good_input_existing_user_but_missing_type():
    from fastapi.testclient import TestClient
    from main import app

    client = TestClient(app)
    response = client.post(
        "/message/collect",
        json={
            "uuid": f"{uuid4()}",
            "customerId": 1,
            "type": "Not Existing Type",
            "amount": "0.13",
        },
    )
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_api_collect_message_with_good_input_missing_type_and_missing_user():
    from fastapi.testclient import TestClient
    from main import app

    client = TestClient(app)
    response = client.post(
        "/message/collect",
        json={
            "uuid": f"{uuid4()}",
            "customerId": 999,
            "type": "Non Existing Type",
            "amount": "0.13",
        },
    )
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_api_collect_message_with_missing_type_param():
    from fastapi.testclient import TestClient
    from main import app

    client = TestClient(app)
    response = client.post(
        "/message/collect",
        json={
            "uuid": f"{uuid4()}",
            "customerId": 999,
            "amount": "0.13",
        },
    )
    assert response.status_code == 422
    assert response.json() != {"status": "ok"}


def test_api_collect_message_with_missing_user_param():
    from fastapi.testclient import TestClient
    from main import app

    client = TestClient(app)
    response = client.post(
        "/message/collect",
        json={
            "uuid": f"{uuid4()}",
            "type": "Non Existing Type",
            "amount": "0.13",
        },
    )
    assert response.status_code == 422
    assert response.json() != {"status": "ok"}


def test_api_collect_message_with_missing_uuid_param():
    from fastapi.testclient import TestClient
    from main import app

    client = TestClient(app)
    response = client.post(
        "/message/collect",
        json={
            "customerId": 999,
            "type": "Non Existing Type",
            "amount": "0.13",
        },
    )
    assert response.status_code == 422
    assert response.json() != {"status": "ok"}


def test_api_collect_message_with_missing_amount_param():
    from fastapi.testclient import TestClient
    from main import app

    client = TestClient(app)
    response = client.post(
        "/message/collect",
        json={
            "uuid": f"{uuid4()}",
            "customerId": 999,
            "type": "Non Existing Type",
        },
    )
    assert response.status_code == 422
    assert response.json() != {"status": "ok"}
