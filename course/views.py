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

		
def course_view(request, name, time, update):
	l = [[el.name, [x for x in Currency.objects.filter(group=el)]] for el in CurrencyGroup.objects.all()]
	group_l = [el.name for el in CurrencyGroup.objects.all()]
	default_picks = 30
	time = int(time)
	time_d = {60: '1 минута', 120: '2 минуты', 180: '3 минуты', 300: '5 минут', 600: '10 минут', 900: '15 минут',
		1800: '30 минут', 3600: '1 час', 7200: '2 часа', 10800: '3 часа', 14400: '4 часа', 21600: '6 часов',
		43200: '12 часов', 85400: '1 день', 604800: '1 неделя'}
	if time not in time_d:
		time = 60
	time_s = time_d[time]
	update = int(update)
	update_d = {1: '1 секунда', 2: '2 секунды', 3: '3 секунды', 5: '5 секунд', 10: '10 секунд', 15: '15 секунд'}
	if update not in update_d:
		update = 1
	update_s = update_d[update]
	return render(request, 'course/course.html', {
		'course_l': l,'groups': group_l, 'name': name.replace('_', ' '), 'name2': name,
		'time': time, 'time_d': time_d.items(), 'time_keys': time_d, 'time_s': time_s,
		'picks': default_picks,
		'update': update, 'update_d': update_d.items(), 'update_keys': update_d, 'update_s': update_s})
	

def course_view_default(request, name):
	default_time = 60
	default_update = 1
	return course_view(request, name, 60, 1)