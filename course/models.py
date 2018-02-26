from django.db import models
from django.utils import timezone

# Create your models here.
class CurrencyGroup(models.Model):
	name = models.CharField(max_length=16, null=True, unique=True,
		help_text='Наименование')
	
	def __str__(self):
		return self.name		
		

class Currency(models.Model):
	name = models.CharField(max_length=16, null=True, unique=True,
		help_text='Наименование валюты')
	group = models.CharField(max_length=16, null=True,
		help_text='Наименование',
		choices=[(el.name, el.name) for el in CurrencyGroup.objects.all()])
		
	def __str__(self):
		return self.name
		
	def name_without_spaces(self):
		return self.name.replace(' ', '_')


class Course(models.Model):
	currency = models.CharField(max_length=16,
		help_text='Наименование валюты',
		choices=[(el.name, tuple(
					(x.name, x.name) for x in Currency.objects.filter(group=el)
				)) for el in CurrencyGroup.objects.all()
			]
		)
	value = models.DecimalField(max_digits=20, decimal_places=10, null=True, default=0.0,
		help_text='Значение')
	time = models.DateTimeField(default=timezone.now,
		help_text='Дата и время')
	prop = models.IntegerField(null=True, default=50, blank=True,
		help_text='Доля участников, ставящих на повышение, %')
	
	def __str__(self):
		return self.currency + ' - ' + self.time.strftime("%A, %d. %B %Y %I:%M%p") + ' ' + str(round(self.value, 10))