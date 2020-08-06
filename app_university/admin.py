from django.contrib import admin
from . import models
from . import forms

class FacultyAdmin(admin.ModelAdmin):
    form = forms.FacultyForm

class CathedraAdmin(admin.ModelAdmin):
    form = forms.CathedraForm

admin.site.register(models.EmployeeModel)
admin.site.register(models.RectorateModel)
admin.site.register(models.FacultyPositionModel)
admin.site.register(models.FacultyModel, FacultyAdmin)
admin.site.register(models.CathedraModel, CathedraAdmin)