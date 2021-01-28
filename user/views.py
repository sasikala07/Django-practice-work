from django.shortcuts import render
### displayed the data into the browser here

from django.http import HttpResponse
from django.template import loader
# Create your views here.
from.models import Contact


def loginpage(request):
    print('Inside login')
    return HttpResponse("<h1 style =color:red>This is login page</h1>")

def registerpge(request):
    return HttpResponse("This is register page")


def contactpage(request):
    if request.method=='GET':
        template = loader.get_template("contact.html")
        return HttpResponse(template.render({}, request))
    else :

        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        email = request.POST['email']
##django shell code
        cont = Contact(first_name=fname, last_name=lname, phone=phone, email=email)
        print (cont)
        cont.save()
        return HttpResponse("Saved your details")