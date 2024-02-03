from pydantic import BaseModel
from typing import Optional

class ResponseModel(BaseModel):
    error: Optional[str] = None
    message: str

class CheckoutResponseModel(ResponseModel):
    book_copy_id: Optional[int] = None

class ReservationResponseModel(ResponseModel):
    reservation_id: int

class BookReturnResponseModel(ResponseModel):
    fine: Optional[str] = ""