from django.contrib import admin
from . import models
from . import forms
# Register your models here.

class RectoratePositionAdmin(admin.ModelAdmin):
    form = forms.RectoratePositionForm

admin.site.register(models.Employee)
admin.site.register(models.RectoratePosition, RectoratePositionAdmin)
admin.site.register(models.FacultyPosition)
admin.site.register(models.Rectorate)
admin.site.register(models.Faculty)
admin.site.register(models.Cathedra)



