from .models import *
from django.shortcuts import render
from django.http import HttpResponse
import datetime, calendar
import json

current_year = int(datetime.datetime.strftime(datetime.datetime.now(), '%y'))
days = {}

def show_event(request):
    current_month = int(datetime.datetime.strftime(datetime.datetime.now(), '%m'))
    num_days = calendar.monthrange(current_year, current_month)[1]
    start_day = datetime.datetime.strftime(datetime.date(2019, current_month, 1), '%w')
    days['start_day'] = start_day

    for day in range(1, num_days+1):
        days[day] = []

    events = Event.objects.all()
    for event in events:
        date = int(datetime.datetime.strftime(event.dates, '%d'))
        days[date].append(event)

    return render(request, 'calendar.html', {'days' : days})

def get_cal(request):
    temp = list(days.keys())
    temp[0] = int(days["start_day"])
    json_data = json.dumps(temp)
    return HttpResponse(json_data, content_type="application/json")
