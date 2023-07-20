from fastapi import APIRouter

from dto_models import CollectMessageDto
from models import Message
from logger import Logger
from repository import UserRepository, MessageRepository, TypeRepository

router = APIRouter()


@router.post("/message/collect")
async def collect_message(messagedto: CollectMessageDto):
    """
    Message collector endpoint.

    Parameters:
        uuid: str = uuid4 type identifier for the message
        type: str = message type
        customerId: int = identifier of the user related to the message
        amount: str = value of the message to generate the statistic values from

    Returns:
        status: str = ok/failed
        error (opt): str = error message
    """
    try:
        user_repository = UserRepository()
        message_repository = MessageRepository()
        type_repository = TypeRepository()

        user = user_repository.get_user_by_customerId(messagedto.customerId)
        message_type = type_repository.get_type(messagedto.type)
        message_bind_object = {
            "uuid": messagedto.uuid,
            "type_id": message_type.uuid,
            "app_user_id": user.uuid,
            "amount": messagedto.amount,
        }
        message_repository.store_message(Message(**message_bind_object))
        return {"status": "ok"}
    except Exception as e:
        Logger.error(str(e))
        return {"status": "failed", "error": str(e)}
