from multiprocessing import context
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

# Create your views here.
def index(request):
    context = {
        'variable1': "sandy is great",
        'variable2': "sandy is mahaan"
    }
    return render(request, 'index.html', context)
    # return HttpResponse("this is a homepage")
def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is a about page")
def contact(request):
    return render(request, 'contact.html')
    #return HttpResponse("this is a contact page")
def services(request):
    return render(request, 'about.html')
    #return HttpResponse("this is a service page")
def servicespubg(request):
    return render(request, 'servicespubg.html')
def add_data(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    dd = {"name":name, "phone": phone, "email": email}
    with open('test.txt',"w") as fh:
        fh.write(str(dd))
    return JsonResponse(dd)
    
    
    
    
    
