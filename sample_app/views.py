from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from sample_app.models import Students

from sample_app.serializers import StudentsSerializer

# Create your views here.


class StudentView(APIView):
    #1. properties
    
    #2. constructor
    
    #3. Method
    def get(self,request, *args, **kwargs):
        result = Students.objects.all()  
        serializers = StudentsSerializer(result, many=True)  
        return Response({'status': 'success', "students":serializers.data}, status=200)  
        pass
    
    #4. Nested Class
    pass
