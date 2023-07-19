from pydantic import BaseModel, validator
import uuid


class CollectMessageDto(BaseModel):
    customerId: int
    type: str
    uuid: str
    amount: str

    @validator("type")
    def type_validator(cls, value):
        if len(value) == 0:
            raise ValueError("Type cannot be empty")
        return value

    @validator("uuid")
    def uuid_validator(cls, value):
        try:
            uuid.UUID(value)
        except ValueError:
            raise ValueError("Invalid UUID")
        return value

    @validator("amount")
    def amount_validator(cls, value):
        if len(value) == 0:
            raise ValueError("Amount cannot be empty")
        try:
            float(value)
        except ValueError:
            raise ValueError("Amount must be a number")
        return value

    @validator("customerId")
    def customerId_validator(cls, value):
        if value < 1:
            raise ValueError("Customer ID must be bigger than 1")
        return value
