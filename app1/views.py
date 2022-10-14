from multiprocessing import context
from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context = {
        'variable1': "sandy is great",
        'variable2': "sandy is mahaan"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("this is a homepage")
def about(request):
    return HttpResponse("this is a about page")
def contact(request):
    return HttpResponse("this is a contact page")
def services(request):
    return HttpResponse("this is a service page")
