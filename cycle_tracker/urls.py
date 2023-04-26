from django.urls import path

from . import views

urlpatterns = [
    path('', views.CycleDatesView.as_view())
]
