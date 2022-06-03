from ast import Import
import imp
from pkgutil import ImpImporter
import re
from urllib import response
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees
from . serializers import employeeserializer

# Create your views here.


class employeeList(APIView):

    def get(self ,request):
        employees1=employees.objects.all()
        serializer=employeeserializer(employees1, many=True)
        return Response(serializer.data)


    def post(self):
        pass
