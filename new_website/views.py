from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'new_website/index.html', {'title': 'Random Lulz Things'})

def resume(request):
    return render(request, 'new_website/resume.html')
