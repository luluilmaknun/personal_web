from django.shortcuts import render

# Create your views here.
def index(request):
    print("masuk")
    return render(request, 'new_website/index.html', {'title': 'Random Lulz Things'})
