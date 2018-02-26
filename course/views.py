from django.shortcuts import render
from .models import Course, Currency, CurrencyGroup

# Create your views here.
def course_list(request):
	l = [[el.name, [x for x in Currency.objects.filter(group=el)]] for el in CurrencyGroup.objects.all()]
	group_l = [el.name for el in CurrencyGroup.objects.all()]
	return render(request, 'course/course_list.html', {'course_l': l, 'groups': group_l})
	

def course_add(request, name, val, prop):
	name = name.replace('_', ' ')
	if(Currency.objects.filter(name=name)):
		new_course = Course(currency=name, value=float(val), prop=int(prop))
		new_course.save()
		return render(request, 'course/course_add.html', {'status': 0})
	else:
		return render(request, 'course/course_add.html', {'status': 1})

		
def course_clear(request, name):
	name = name.replace('_', ' ')
	if name == 'all':
		Course.objects.all().delete()
		return render(request, 'course/course_clear.html', {'status': 0})
	elif Currency.objects.filter(name=name):
		Course.objects.filter(currency=name).delete()
		return render(request, 'course/course_clear.html', {'status': 0})
	else:
		return render(request, 'course/course_clear.html', {'status': 1})
		
def course_view(request, name):
	l = [[el.name, [x for x in Currency.objects.filter(group=el)]] for el in CurrencyGroup.objects.all()]
	group_l = [el.name for el in CurrencyGroup.objects.all()]
	return render(request, 'course/course.html', {'course_l': l, 'groups': group_l, 'name': name.replace('_', ' '), 'name2': name})