from .models import *
from django.shortcuts import render
from django.http import HttpResponse
import datetime, calendar
import json

current_year = int(datetime.datetime.strftime(datetime.datetime.now(), '%y'))
current_month = int(datetime.datetime.strftime(datetime.datetime.now(), '%m'))
days = {}
start_day = int(datetime.datetime.strftime(datetime.date(2019, current_month, 1), '%w'))
days['start_day'] = start_day

def show_event(request):
    num_days = calendar.monthrange(current_year, current_month)[1]

    for day in range(1, num_days+1):
        days[day] = []

    events = Event.objects.all()
    for event in events:
        date = int(datetime.datetime.strftime(event.dates, '%d'))
        days[date].append(event)

    make_cal()

    return render(request, 'calendar.html', {'days' : days})

def get_cal(request):
    temp = list(days.keys())
    json_data = json.dumps(temp)
    return HttpResponse(json_data, content_type="application/json")

def make_cal():
    f = open("ToDo/templates/calendar_entry.html", "+w")
    column = 0
    row = 0
    text = "<tr id= " + str(row) + ">"
    for i in range(0, start_day):
        text += "<td id= " + str(column) + " height='100' " + ">  </td>"
        column = column + 1

    for i in range(1, len(days)):
        if column > 6:
            column = 0
            row = row + 1
            text += "</tr><tr id= " + str(row) + ">"
        text += "<td id= " + str(column) + " height='100' " + "> " + str(i)
        text += "{% if days." + str(i) +  " %}"
        text += "{% for event in days." + str(i) +  " %}<ul>"
        text += "<li>{{ event.title }}</li>"
        text += "</ul>{% endfor %}{% endif %}</td>"
        column = column + 1

    text += "</tr>"
    f.write(text)
    f.close()
