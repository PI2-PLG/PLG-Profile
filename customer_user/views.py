from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from customer_user.models import CustomerUser
import io

@api_view(['GET', 'POST'])
def get_user(request):
        print(request.data['username'])
        try:
                if request.method == 'POST':
                        username = request.data['username']
                        password = request.data['password']

                        user = CustomerUser(username=username, password=password)
                        user.save()

                        response = "{ response: ok }"
                        return Response(response,status=status.HTTP_201_CREATED)
        except:

                response = "{ response: not-ok }"
                return Response(response,status=status.HTTP_201_CREATED)
