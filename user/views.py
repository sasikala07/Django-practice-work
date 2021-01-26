from django.shortcuts import render
### displayed the data into the browser here

from django.http import HttpResponse
# Create your views here.
def loginpage(request):
    print('Inside login')
    return HttpResponse("<h1 style =color:red>This is login page</h1>")

def registerpge(request):
    return HttpResponse("This is register page")