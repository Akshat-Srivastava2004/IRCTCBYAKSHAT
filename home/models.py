from django.db import models
class passengerdetail(models.Model):
    passengername=models.CharField(max_length=50)
    Destination=models.CharField(max_length=50)
    Trainnumber=models.IntegerField(null=True)
    Tickets=models.IntegerField(null=True)
    Phonenumber=models.IntegerField(null=True)
