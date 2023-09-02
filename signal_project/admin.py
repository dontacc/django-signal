from django.contrib import admin
from .models import Students



@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ("name",)