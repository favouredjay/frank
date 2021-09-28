from django.shortcuts import render, redirect

# Create your views here.
from cohorts.forms import CohortForm, NativeForm
from cohorts.models import Cohort


def all_cohorts(request):
    cohorts = Cohort.objects.all()
    akeem = {
        "cohorts": cohorts
    }
    return render(request, "cohorts/hello_world.html", akeem)


def create_cohort(request):
    form = CohortForm()
    if request.method == "POST":
        form = CohortForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cohorts')
        else:
            context = {
                "error": form.errors
            }
            return render(request, "joy/error_page.html", context)
    else:
        return render(request, "joy/hello_world.html", context={"form": form})


def create_native(request):
    form = NativeForm()
    if request.method == "POST":
        form = NativeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "natives.html")
        else:
            context = {
                "error": form.errors
            }
            return render(request, "joy/error_page.html", context)
    else:
        return render(request, "native_form.html", {"form": form})
