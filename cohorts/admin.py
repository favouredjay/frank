from django.contrib import admin

# Register your models here.
from cohorts.models import Cohort


class CohortAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "date_created")


admin.site.register(Cohort, CohortAdmin)
