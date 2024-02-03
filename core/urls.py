from django.urls import re_path
from .views import Checkout, Reserve, Return

urlpatterns = [
    re_path(r"^checkout/$", Checkout.as_view(), name='checkout_book'),
    re_path(r"^reserve/$", Reserve.as_view(), name='reserve_book'),
    re_path(r"^return/$", Return.as_view(), name='return_book'),
]
