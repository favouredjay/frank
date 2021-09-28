from django.urls import path

from . import views

urlpatterns = [
    path('', views.all_cohorts, name='cohorts'),
    path('create', views.create_cohort, name="create_cohort"),
    path('create_native/', views.create_native, name="create_native"),
]
