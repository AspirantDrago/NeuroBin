from django.shortcuts import render
from .models import Course, Currency

# Create your views here.
def course_list(request):
    return render(request, 'course/course_list.html', {})
	

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
	if(Currency.objects.filter(name=name)):
		Course.objects.filter(currency=name).delete()
		return render(request, 'course/course_clear.html', {'status': 0})
	else:
		return render(request, 'course/course_clear.html', {'status': 1})