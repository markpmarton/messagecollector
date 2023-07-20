from pydantic import BaseModel, field_validator
import uuid


class CollectMessageDto(BaseModel):
    """
    Input data transfer object for the collector API.
    """

    customerId: int
    type: str
    uuid: str
    amount: str

    @field_validator("type")
    def type_validator(cls, value):
        if len(value) == 0:
            raise ValueError("Type cannot be empty")
        return value

    @field_validator("uuid")
    def uuid_validator(cls, value):
        try:
            uuid.UUID(value)
        except ValueError:
            raise ValueError("Invalid UUID")
        return value

    @field_validator("amount")
    def amount_validator(cls, value):
        if len(value) == 0:
            raise ValueError("Amount cannot be empty")
        try:
            float(value)
        except ValueError:
            raise ValueError("Amount must be a number")
        return value

    @field_validator("customerId")
    def customerId_validator(cls, value):
        if value < 1:
            raise ValueError("Customer ID must be bigger than 1")
        return value
