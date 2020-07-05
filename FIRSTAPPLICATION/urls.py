from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:domain_id>/', views.training_domain, name="domain"),
    path('<int:domain_id>/candidate/', views.candidate, name="candidate"),
]