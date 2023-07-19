from datetime import datetime

from config import TIME_FORMAT, DB_CONN_STR
from models import User, Type, Message

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class MessageRepository:
    def __init__(self):
        self.engine = create_engine(DB_CONN_STR)

    def get_messages_by_user_and_type(
        self, customer_id: int, message_type: str, from_time: str, to_time: str
    ) -> list:
        with Session(self.engine) as session:
            filtered = session.query(Message).filter(
                Message.received_at >= datetime.strptime(from_time, TIME_FORMAT)
            )
            if to_time == "":
                filtered.filter(Message.received_at <= datetime.now())
            else:
                filtered.filter(
                    Message.received_at <= datetime.strptime(to_time, TIME_FORMAT)
                )
            if customer_id > 0:
                user = (
                    session.query(User).filter(User.customerid == customer_id).first()
                )
                if not user:
                    return []
                filtered = filtered.filter(Message.app_user_id == user.uuid)
            if message_type != "":
                msg_type = session.query(Type).filter(Type.name == message_type).first()
                if not msg_type:
                    return []
                filtered = filtered.filter(Message.type_id == msg_type.uuid)

        return filtered.all()
