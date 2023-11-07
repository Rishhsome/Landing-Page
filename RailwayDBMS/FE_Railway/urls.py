from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submit/railway_system/', views.submit_railway_system, name='submit_railway_system'),
    path('submit/railway/', views.submit_railway, name='submit_railway'),
    path('submit/train/', views.submit_train, name='submit_train'),
]