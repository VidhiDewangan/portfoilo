from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', )  # columns to show
    search_fields = ('name', )        # search bar
    list_filter = ('age',)                   # filter sidebar

admin.site.register(Student, StudentAdmin)