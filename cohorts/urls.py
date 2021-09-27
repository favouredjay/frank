from django.urls import path

from . import views

urlpatterns = [
    path('anything', views.hello_world),
    path('otherthings', views.create_cohort),
]
