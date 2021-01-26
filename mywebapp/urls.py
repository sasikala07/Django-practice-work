"""mywebapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.template import loader

def mypage(request):
    print('Inside mypage')
    return HttpResponse("<h1 style =color:red>This is my webpage</h1>")

##home page
def myhome(request):
    template=loader.get_template("home.html")
    return HttpResponse(template.render({},request))
##by default template
## to change the folder template name to another folder name ..we havr to ad d the name into
##settings.py TEMPLATES DIR=['content'] content is the folder name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome',mypage) ,## /welcome/ is the path for print mypage data
    path('user/', include('user.urls')),
    path('product/', include('product.urls')),
    path('home/',myhome),
    path('cart/',include('cart.urls'))

]



