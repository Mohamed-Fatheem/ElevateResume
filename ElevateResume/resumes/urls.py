from django.urls import path
from . import views

urlpatterns = [
    path('', views.resume_list, name='resume_list'),
    path('new/', views.resume_form, name='resume_form'),
    path('<int:id>/pdf/', views.generate_pdf, name='resume_pdf'),
]
