from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(BookCopy)
admin.site.register(Member)
admin.site.register(Reservation)
admin.site.register(ReservationLiveStatus)
admin.site.register(ReservationLiveStatusHistory)
admin.site.register(Checkout)
admin.site.register(BookAvailabilityStatus)
admin.site.register(BookAvailabilityStatusHistory)
