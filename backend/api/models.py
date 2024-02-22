from django.db import models
import datetime
# Create your models here.
class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=100, unique=True, blank=False, null=False)
    copies = models.IntegerField(default=1)
        
    
class Members(models.Model):
    member_id = models.AutoField(primary_key=True)
    member_name = models.CharField(max_length=100)

class Circulation(models.Model):
    returnevent = models.BooleanField(default=False)
    book_id = models.IntegerField()
    member_id = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True, blank=False)
    returndate = models.DateTimeField( default = datetime.datetime.now(), blank=True, null=True)