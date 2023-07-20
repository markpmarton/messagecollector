from datetime import datetime

from config import TIME_FORMAT, DB_CONN_STR, MIN_TIME
from logger import Logger
from models import User, Type, Message

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


class MessageRepository:
    """
    Handles message related db transactions
    """

    def __init__(self):
        self.engine = create_engine(DB_CONN_STR)

    def get_messages_by_user_and_type(
        self, customer_id: int, message_type: str, from_time: str, to_time: str
    ) -> list:
        try:
            with Session(self.engine) as session:
                filtered = session.query(Message)
                Logger.info(
                    f"from_time: {from_time}, to_time: {to_time}, id: {customer_id}, type: {message_type}"
                )
                Logger.info(filtered.all())
                if from_time != MIN_TIME:
                    filtered = filtered.filter(
                        Message.received_at >= datetime.strptime(from_time, TIME_FORMAT)
                    )
                if to_time != "":
                    filtered = filtered.filter(
                        Message.received_at <= datetime.strptime(to_time, TIME_FORMAT)
                    )
                if customer_id > 0:
                    user = (
                        session.query(User)
                        .filter(User.customerid == customer_id)
                        .first()
                    )
                    if not user:
                        return []
                    filtered = filtered.filter(Message.app_user_id == user.uuid)
                if message_type != "":
                    msg_type = (
                        session.query(Type).filter(Type.name == message_type).first()
                    )
                    if not msg_type:
                        return []
                    filtered = filtered.filter(Message.type_id == msg_type.uuid)

            return filtered.all()
        except Exception as e:
            Logger.error(str(e))
            return []
