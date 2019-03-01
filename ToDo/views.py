from .models import *
from django.shortcuts import render
import datetime, calendar

current_year = int(datetime.datetime.strftime(datetime.datetime.now(), '%y'))

def show_cal(request):
    current_month = int(datetime.datetime.strftime(datetime.datetime.now(), '%m'))
    num_days = calendar.monthrange(current_year, current_month)[1]
    days = {}
    for day in range(1, num_days+1):
        days[day] = []

    events = Event.objects.all()
    for event in events:
        date = int(datetime.datetime.strftime(event.dates, '%d'))
        days[date].append(event)

    return render(request, 'calendar.html', {'days' : days})
