from django.db import models
from django.utils import timezone

# Create your models here.
class Predict(models.Model):
	currency = models.CharField(max_length=16, null=True,
		help_text='Наименование валюты')
	value = models.DecimalField(max_digits=20, decimal_places=10, null=True, default=0.0,
		help_text='Предсказанное значение')
	time = models.DateTimeField(
		help_text='Дата и время')
	is_call = models.NullBooleanField(null=True, blank=True,
		help_text='Будет ли повышение')
	chahce = models.FloatField(null=True, blank=True,
		help_text='Вероятность')
	from_time = models.DateTimeField(default=timezone.now,
		help_text='Дата и время предсказания')
	
	def __str__(self):
		return self.currency + ' - от ' + self.from_time.strftime("%A, %d. %B %Y %I:%M%p") \
			+ ' на ' + self.time.strftime("%A, %d. %B %Y %I:%M%p") + ' ' + str(round(self.value, 10))