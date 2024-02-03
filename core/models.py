from django.db import models


RESERVATION_STATUS_OPTIONS = (
    ('QUEUED', 'QUEUED'),
    ('FULFILLED', 'FULFILLED')
)

CHECKOUT_STATUS_OPTIONS = (
    ('AVAILABLE', 'AVAILABLE'),
    ('CHECKED_OUT', 'CHECKED_OUT'),
    ('RETURNED', 'RETURNED')
)

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=100, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

class Book(models.Model):
    title = models.CharField(max_length=100, unique=True, db_index=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

class BookCopy(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

class Member(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

class Reservation(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    days=models.IntegerField(default=1)

class ReservationLiveStatus(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=RESERVATION_STATUS_OPTIONS, default=RESERVATION_STATUS_OPTIONS[0][1], db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

class ReservationLiveStatusHistory(models.Model):
    live_status = models.ForeignKey(ReservationLiveStatus, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=RESERVATION_STATUS_OPTIONS, default=RESERVATION_STATUS_OPTIONS[0][1], db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

class Checkout(models.Model):
    book_copy = models.ForeignKey(BookCopy, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    end_at = models.DateTimeField(db_index=True)

class BookAvailabilityStatus(models.Model):
    book_copy = models.ForeignKey(BookCopy, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=CHECKOUT_STATUS_OPTIONS, default=CHECKOUT_STATUS_OPTIONS[0][1], db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

class BookAvailabilityStatusHistory(models.Model):
    checkout_status = models.ForeignKey(BookAvailabilityStatus, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=CHECKOUT_STATUS_OPTIONS, default=CHECKOUT_STATUS_OPTIONS[0][1], db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)