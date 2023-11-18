from django.urls import path
from . import views


urlpatterns = [
    path('events', views.list),
    path('events/<int:pk>', views.detail),
]
