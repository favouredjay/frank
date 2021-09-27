from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from cohorts.models import Cohort


def hello_world(request):
    cohort = Cohort.objects.get(id=4)
    print(cohort)
    variable = "value"
    akeem = {
        "anything": variable
    }
    return render(request, "cohorts/hello_world.html", akeem)


def create_cohort(request):
    return render(request, "joy/hello_world.html")
