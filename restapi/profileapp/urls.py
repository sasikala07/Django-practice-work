from django.contrib import admin
from django.urls import path
from .views import ProfileListView,ProfileDetailView

urlpatterns = [
    path('api/profiles', ProfileListView.as_view()),
    path('api/profiles/<str:id>',ProfileDetailView.as_view())
]
