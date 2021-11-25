from django.urls import path
from applovecalculator import views
urlpatterns = [
    path('',views.IndexView.as_view(),name="Index" ),
    path('event',views.EventView.as_view(),name="Event" ),
]