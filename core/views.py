from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .configs.responsemodels import ResponseModel
from .models import *
from .controllers.checkoutcontroller import CheckoutController
from .controllers.reservationcontroller import ReservationController
from .controllers.returncontroller import ReturnController

# Create your views here.
class Checkout(APIView):
    def post(self, request):
        member_id = request.data.get('member_id')
        book_id = request.data.get('book_id')
        days = request.data.get('days')

        error_response = None
        member = None
        book=None

        if member_id is None or book_id is None or days is None:
            error_response = ResponseModel(
                error="Missing member_id / book_id or return_date",
                message="Please provide valid member_id, book_id and return_date"
            )
        
        try:
            member = Member.objects.get(id=member_id)
            book = Book.objects.get(id=book_id)
        except Member.DoesNotExist:
            error_response = ResponseModel(
                error="Invalid member_id",
                message="Please provide a valid member_id"
            )
        except Book.DoesNotExist:
            error_response = ResponseModel(
                error="Invalid book_id",
                message="Please provide a valid book_id"
            )
        
        if error_response is not None:
            return Response(
                error_response.model_dump(),
                status=status.HTTP_400_BAD_REQUEST
            )
        
        controller = CheckoutController(
            book=book,
            member=member,
            days=days,
        )

        response = controller.get_response()

        return Response(response, status=status.HTTP_200_OK)


class Reserve(APIView):
    def post(self, request):
        member_id = request.data.get('member_id')
        book_id = request.data.get('book_id')
        days = request.data.get('days')

        error_response = None
        member = None
        book=None

        if member_id is None or book_id is None or days is None:
            error_response = ResponseModel(
                error="Missing member_id / book_id or days",
                message="Please provide valid member_id, book_id"
            )
        
        try:
            member = Member.objects.get(id=member_id)
            book = Book.objects.get(id=book_id)
        except Member.DoesNotExist:
            error_response = ResponseModel(
                error="Invalid member_id",
                message="Please provide a valid member_id"
            )
        except Book.DoesNotExist:
            error_response = ResponseModel(
                error="Invalid book_id",
                message="Please provide a valid book_id"
            )
        
        if error_response is not None:
            return Response(
                error_response.model_dump(),
                status=status.HTTP_400_BAD_REQUEST
            )
        
        controller = ReservationController(
            member=member,
            book=book,
            days=days,
        )

        response = controller.get_response()

        return Response(response, status=status.HTTP_200_OK)


class Return(APIView):
    def post(self, request):
        book_copy_id = request.data.get('book_copy_id')
        member_id = request.data.get('member_id')

        member = None
        book_copy = None
        error_response = None

        if member_id is None or book_copy_id is None:
            error_response = ResponseModel(
                error="Missing member_id / book_id or return_date",
                message="Please provide valid member_id, book_id"
            )
        
        try:
            member = Member.objects.get(id=member_id)
            book_copy = BookCopy.objects.get(id=book_copy_id)
        except Member.DoesNotExist:
            error_response = ResponseModel(
                error="Invalid member_id",
                message="Please provide a valid member_id"
            )
        except BookCopy.DoesNotExist:
            error_response = ResponseModel(
                error="Invalid book_id",
                message="Please provide a valid member_id"
            )
        
        if error_response is not None:
            return Response(
                error_response.model_dump(),
                status=status.HTTP_400_BAD_REQUEST
            )
        
        controller = ReturnController(
            book_copy=book_copy,
            member=member
        )

        response = controller.get_response()

        return Response(response, status=status.HTTP_200_OK)

# class OverDueBooks(APIView):
#     def get(self, request):
#         member_id = request.query_params.get('member_id')