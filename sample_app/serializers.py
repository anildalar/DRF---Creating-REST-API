from sample_app.models import Students
from rest_framework import serializers

class StudentsSerializer(serializers.ModelSerializer):
    firstname = serializers.CharField(max_length=200, required=True)  
    lastname = serializers.CharField(max_length=200, required=True)  
    address = serializers.CharField(max_length=200, required=True)  
    roll_number = serializers.IntegerField()  
    mobile = serializers.CharField(max_length=10, required=True)  
    
    #3. Method area
    def create(self,validated_data):
        
        #create
        student = Students.objects.create(**validated_data)
        # every function return something
        return student
        pass
    
    def update(self):
        pass
    
    #4. Nested Class
    class Meta():
        #1. property
        model = Students
        fields = ('__all__')
        
        pass
    pass