from .models import *
from .forms import *
from django.shortcuts import render, redirect
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
        freq = event.freq
        date = int(datetime.datetime.strftime(event.dates, '%d'))
        days[date].append(event)

    make_cal()
    forms = EventForm()

    return render(request, 'calendar.html', {'days' : days, 'forms': forms})

def add_event(request):
    form = EventForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('show_event')

def make_cal():
    f = open("ToDo/templates/calendar_entry.html", "+w")
    column = 0
    row = 0
    text = "<tr id= " + str(row) + ">"
    for i in range(0, start_day):
        text += "<td id= " + str(column) + " height='150' " + ">  </td>"
        column = column + 1

    for i in range(1, len(days)):
        if column > 6:
            column = 0
            row = row + 1
            text += "</tr><tr id= " + str(row) + ">"
        if i%2 == 0:
            text += "<td id= " + str(column) + " class='green' height='150' " + "> " + str(i)
        else:
            text += "<td id= " + str(column) + " height='150' " + "> " + str(i)
        text += "{% if days." + str(i) +  " %}"
        text += "{% for event in days." + str(i) +  " %}<ul>"
        text += "<li>{{ event.title }}</li>"
        text += "</ul>{% endfor %}{% endif %}</td>"
        column = column + 1

    text += "</tr>"
    f.write(text)
    f.close()
