from django.contrib import admin
from django.urls import path
from ncpordata import views
from . import views



urlpatterns = [
    path("",views.index,name='ncpordata'),
    path("about/",views.about,name='about'),
    path("services/",views.services,name='services'),
    path("polardirectory/",views.polardirectory,name='polardirectory'),
    path("datasubmission/",views.datasubmission,name='datasubmission'),
    path('success/<int:pk>/', views.success, name='success'),
    path('get-states/', views.get_states, name='get_states'),
    path('get-topics/', views.get_topics, name='get_topics'),
    
]