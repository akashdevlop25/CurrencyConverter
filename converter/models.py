from django.db import models

class Data(models.Model):
	currency1 = models.CharField(max_length=3, default='PLN')
	currency2 = models.CharField(max_length=3, default='EUR')
	amount = models.IntegerField(default=100)