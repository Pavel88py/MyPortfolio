from django.shortcuts import render

# Create your views here.


def home(request):
    name = 'Coco Channel'
    return render(request, 'index.html', {'name': name})


def work(request):
    return render(request, 'work.html')


def contact(request):
    return render(request, 'contact.html')


def home2(request):
    return render(request, 'index2.html')