from django.contrib import admin

# Register your models here.
from cohorts.models import Cohort, Native


# @admin.register(Cohort)
class CohortAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "date_created")


# @admin.register(Native)
class NativeAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "cohort")


admin.site.register(Cohort, CohortAdmin)
admin.site.register(Native, NativeAdmin)
