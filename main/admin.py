from django.contrib import admin
from .models.main_model import SaveConcreate, Registration


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "phone"]


@admin.register(SaveConcreate)
class SaveConcreteAdmin(admin.ModelAdmin):
    list_display = ["data", "factory_name", "object_name",
                    "block", "mark", "constructive", "floor",
                    "fact_concrete", "sum_concrete", "accepted"]