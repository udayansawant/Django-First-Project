from django.db import models

class FirstApp(models.Model):
    Name = models.CharField(max_length=100)
    ID = models.AutoField
    Contact = models.IntegerField
    Address = models.CharField(max_length=100)
    