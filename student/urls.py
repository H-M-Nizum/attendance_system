from django.urls import path
from . import views

urlpatterns = [
    
    path('add/', views.Addstudent.as_view(), name='add_student'),
    path('', views.showstudent, name='showstudent'),
    path('classs/<slug:class_slug>/', views.showstudent, name='class_slug_student'),
    
]