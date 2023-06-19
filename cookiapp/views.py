from django.shortcuts import render
from django.http import HttpResponse
#from django.views import View
# Create your views here.
def home(request):
    return render(request,'input.html')
def calculate(request):
    x=request.GET["t1"]
    y=request.GET["t2"]
    z=int(x)+int(y)
    res=HttpResponse("data sunmitted successfully")
    res.set_cookie('z',z,max_age=100)
    return res
def display(request):
    if 'z' in request.COOKIES:
        res=request.COOKIES['z']
        return HttpResponse("the sum is:"+res)
    else:
        return render(request,'input.html')