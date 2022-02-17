from django.db import models

class Employee(models.Model):
	name=models.CharField(max_length=20)
	age=models.CharField(max_length=20)
	esal=models.FloatField()
	eaddr=models.CharField(max_length=30)
