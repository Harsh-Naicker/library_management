from ..models import *
from ..configs.responsemodels import BookReturnResponseModel
from datetime import datetime

class ReturnController:
    def __init__(self, book_copy: BookCopy, member: Member) -> None:
        self.book_copy = book_copy
        self.member = member
    
    def get_response(self) -> BookReturnResponseModel:
        # Find the corresponding checkout entry

        checkout = Checkout.objects.filter(
            book_copy=self.book_copy,
            member=self.member
        ).order_by("-id").first()

        if checkout is not None:
            end_date = checkout.end_at
            fine = 0
            delta = (datetime.now().date() - end_date.date()).days

            if delta > 0:
                fine = delta*50
            
            availability_status = BookAvailabilityStatus.objects.get(
                book_copy = self.book_copy
            )
            availability_status.status = CHECKOUT_STATUS_OPTIONS[2][1]
            availability_status.save()

            availability_status_history = BookAvailabilityStatusHistory.objects.create(
                checkout_status=availability_status,
                member=self.member,
                status=CHECKOUT_STATUS_OPTIONS[2][1]
            )

            # Push kafka event for checking queue reservations and doing a system
            # checkout

            
            response = BookReturnResponseModel(
                fine=f"Rs. {fine}",
                message="Thank you for returning the book"
            ).model_dump()

            return response

        return BookReturnResponseModel(
            message="Cannot find checkout records"
        ).model_dump()

        