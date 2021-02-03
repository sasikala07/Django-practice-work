from rest_framework import routers
from .views import TaskView
from django.urls import path, include

router = routers.DefaultRouter()
router.register('tasks',TaskView)

urlpatterns = [
   path('test/', include(router.urls))  ##test url shows default django rest framework
]

##/api/test/tasks/