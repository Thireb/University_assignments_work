from django.urls import path
from .views import homeView, displayView

urlpatterns = [
    path('',homeView,name='home'),
    path('display',displayView,name='display'),
]
