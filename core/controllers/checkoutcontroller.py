from ..models import *
from ..configs.responsemodels import CheckoutResponseModel
from datetime import datetime, timedelta

class CheckoutController:
    def __init__(self, book: Book, member: Member, days: int) -> None:
        self.book: Book = book
        self.member: Member = member
        self.days = days
    
    def get_response(self) -> CheckoutResponseModel:
        book_copy_availability: BookAvailabilityStatus = BookAvailabilityStatus.objects.filter(
            book_copy__book=self.book,
            status__in=[CHECKOUT_STATUS_OPTIONS[0][1], CHECKOUT_STATUS_OPTIONS[2][1]]
        ).order_by('book_copy__id').first()

        if book_copy_availability is not None:
            # check the book out
            book_copy: BookCopy = book_copy_availability.book_copy

            end_at = datetime.now() + timedelta(days=self.days)

            checkout = Checkout.objects.create(
                book_copy=book_copy,
                member=self.member,
                end_at=end_at,
            )

            checkout_status = BookAvailabilityStatus.objects.get(
                book_copy=book_copy,
            )

            checkout_status.status = CHECKOUT_STATUS_OPTIONS[1][1]
            checkout_status.save()

            checkout_status_history = BookAvailabilityStatusHistory.objects.create(
                checkout_status=checkout_status,
                member = self.member,
                status = CHECKOUT_STATUS_OPTIONS[1][1]
            )

            return CheckoutResponseModel(
                book_copy_id=book_copy.id,
                message="Book has been checked out succcessfully",
            ).model_dump()
        
        return CheckoutResponseModel(
            message="This book is not available right now, please make a reservation"
        ).model_dump()
    