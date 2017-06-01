
from django.http import HttpResponse
from .models import User, Helper
from .serializer import UserSerializer
from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.http import JsonResponse
import requests
import json


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @detail_route()
    def getFolders(self, request, email):
        """ Returns a list of location objects somehow related to MyObject """
        try:
            validate_email(email)
        except ValidationError:
            return Response({'message':'Email is Not Valid'})
        response = requests.get('https://demo1419375.mockable.io/'+email)
        return Response(response)

    @detail_route()
    def getFoldersDetails(self, request, email, folder):
        """ Returns a list of location objects somehow related to MyObject """
        try:
            validate_email(email)
        except ValidationError:
            return Response({'message': 'Email is Not Valid'})
        folderList = requests.get('https://demo1419375.mockable.io/' + email)
        for x in folderList:
            if x == folder:
                return Response({'message':'Folder Found'})
        return Response({'message':'Folder Not Found'})

    @detail_route()
    def getHelperForFolder(self, request, email, folder):
        """ Returns a list of location objects somehow related to MyObject """
        try:
            validate_email(email)
        except ValidationError:
            return JsonResponse({'message': 'Email is Not Valid'})
        #return HttpResponse(folder)
        helperList = Helper.objects.filter(connected_email=email,connected_folder=folder)
        response = []
        for x in helperList:
            response.append(x.user.first_name)
        return Response(response)
