from config import TIME_FORMAT, MIN_TIME

from fastapi import APIRouter
from datetime import datetime

from repository import MessageRepository

router = APIRouter()


@router.get("/stats")
async def get_stats(
    customerId: int = 0,
    msg_type: str = "",
    from_time: str = MIN_TIME,
    to_time: str = "",
):
    try:
        message_repository = MessageRepository()
        messages = message_repository.get_messages_by_user_and_type(
            customerId, msg_type, from_time, to_time
        )

        amounts = [float(message.amount) for message in messages]

        response_stats = {"msg": {"count": len(messages)}}

        if len(messages) > 0:
            response_stats["msg"]["first"] = {
                "uuid": messages[0].uuid,
                "timestamp": messages[0].received_at.strftime(TIME_FORMAT),
            }
            response_stats["msg"]["last"] = {
                "uuid": messages[-1].uuid,
                "timestamp": messages[-1].received_at.strftime(TIME_FORMAT),
            }
            response_stats["amount"] = {
                "total": sum(amounts),
                "avg": sum(amounts) / len(messages),
                "max": max(amounts),
                "min": min(amounts),
            }
        return {"status": "ok", "data": response_stats}
    except Exception as e:
        return {"status": "failed", "error": str(e)}
