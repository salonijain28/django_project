from django.db import models

# Create your models here.
class Mycontact(models.Model):
    your_name=models.CharField(max_length=30)
    your_email=models.EmailField(max_length=254)
    Subject=models.CharField(max_length=50)
    Message=models.CharField(max_length=250)
