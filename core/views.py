################# Libs #################
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from . import models
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .serializer import GeneralinfoSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.mail import mail_admins, send_mail, BadHeaderError, EmailMessage
import requests

#######################################

class GeneralinfoView(ModelViewSet):
        queryset = models.GeneralInfo.objects.all()
        serializer_class = GeneralinfoSerializer
        permission_classes = [IsAuthenticated]

        def get_permissions(self):
                if self.request.method =='GET':
                         return [AllowAny()]
                return [IsAuthenticated()]

        
def SendEmail(request):
        try:
                message = EmailMessage('test subject', 'new messageeeeeeeeeee',
                           'info@cpm.com', ['kasra@gmail.com'])
                message.attach_file('core/static/images/test.jpg')
                message.attach
                message.send()
                # send_mail('test subject', 'new messageeeeeeeeeee',
                #            'info@cpm.com', ['kasra@gmail.com'])
        except BadHeaderError:
                pass

        #return render(request, 'hello.html', {'name': 'Kasra'})
        return HttpResponse('email has been sent !')


@cache_page(5*10)
def TestCaching(request):
        response = requests.get('https://httpbin.org/delay/3')
        data = response.json()
        return HttpResponse('test (get) request has been sent !',data)

