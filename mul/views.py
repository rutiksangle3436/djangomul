from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def mult(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    res = val1 * val2

    return render(request,'mul.html',{'result':res})