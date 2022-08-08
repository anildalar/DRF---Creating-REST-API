from django.db import models

# Create your models here.

class Students(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    address = models.TextField()
    roll_number = models.IntegerField()
    mobile = models.CharField(max_length=20)
    
    #3. Member
    def __str__(self):
        return self.firstname
    pass

