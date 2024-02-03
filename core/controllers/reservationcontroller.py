from ..models import *
from ..configs.responsemodels import ReservationResponseModel

class ReservationController:
    def __init__(self, member: Member, book: Book, days: int) -> None:
        self.member = member
        self.book = book
        self.days = days
    
    def get_response(self):
        pending_reservation = ReservationLiveStatus.objects.filter(
            reservation__book=self.book,
            reservation__member=self.member,
            status__in=[RESERVATION_STATUS_OPTIONS[0][1]]
        ).exists()

        if not pending_reservation:
            reservation = Reservation.objects.create(
                book=self.book,
                member=self.member,
                days=self.days,
            )

            reservation_live_status = ReservationLiveStatus.objects.create(
                reservation=reservation
            )

            ReservationLiveStatusHistory.objects.create(
                live_status=reservation_live_status,
                status=RESERVATION_STATUS_OPTIONS[0][1]
            )

            return ReservationResponseModel(
                reservation_id=reservation.id,
                message="Your reservation has been queued successfully"
            ).model_dump()
        
        return ReservationResponseModel(
            message="You already have a pending reservation for this book"
        ).model_dump()