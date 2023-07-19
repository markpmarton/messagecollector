from datetime import datetime

from config import DB_CONN_STR
from models import User, Message, Type

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class UserRepository:
    def __init__(self):
        self.engine = create_engine(DB_CONN_STR)

    def get_user_by_customerId(self, customerId: int) -> User:
        with Session(self.engine) as session:
            user = session.query(User).filter_by(customerid=customerId).first()
            if not user:
                user = User(
                    created_at=datetime.now(),
                    name=f"User {customerId}",
                )
                session.add(user)
                session.commit()

        with Session(self.engine) as session:
            user = session.query(User).filter_by(customerid=customerId).first()
            return user


class TypeRepository:
    def __init__(self):
        self.engine = create_engine(DB_CONN_STR)

    def get_type(self, name: str) -> Type:
        with Session(self.engine) as session:
            act_type = session.query(Type).filter_by(name=name).first()
            if not act_type:
                act_type = Type(
                    name=f"{name}",
                )
                session.add(act_type)
                session.commit()
        with Session(self.engine) as session:
            act_type = session.query(Type).filter_by(name=name).first()
            return act_type


class MessageRepository:
    def __init__(self):
        self.engine = create_engine(DB_CONN_STR)

    def message_exists(self, uuid: str) -> bool:
        with Session(self.engine) as session:
            return session.query(Message).filter_by(uuid=uuid).first() is not None

    def store_message(self, msg: Message):
        with Session(self.engine) as session:
            if self.message_exists(msg.uuid):
                # dropping already stored message
                return
            session.add(msg)
            session.commit()
