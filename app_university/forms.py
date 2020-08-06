from app_university.models import *
from django import forms

# class RectoratePositionForm(forms.ModelForm):

#     position_title = forms.CharField(max_length=70, label='Должность')
#     belong_id = forms.ChoiceField(choices=(), required=True, label='В подчинении у')
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)  
#         r = models.RectoratePosition.objects.all()
#         self.choices = []
#         if(not len(r)):
#             newPosition = models.RectoratePosition(position_title="без подчинения")
#             newPosition.save()
#             x = models.RectoratePosition.objects.get(id=newPosition.id)
#             print(x)
#             self.fields['belong_id'].choices = [(x, x)]
#         else:
#             for item in r:
#                 self.choices.append((item, item))
#                 self.fields['belong_id'].choices = self.choices


#Формы, созданные с единственной целью: отображать список сотрудников, которые могут занимать пост(по разным условиям)
#Посколько по умолчанию отображаются все сотрудники
class FacultyForm(forms.ModelForm):

    header_faculty = forms.ModelChoiceField(EmployeeModel.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if ('instance' in kwargs) and (kwargs['instance'] is not None):
            self.fields['header_faculty'].queryset = EmployeeModel.objects.filter(
                fk_faculties=kwargs['instance'].id,
                rectorate_position__isnull=True,
                faculty_position__isnull=True,
                cathedra_position__isnull=True
            )

class CathedraForm(forms.ModelForm):

    header_cathedra = forms.ModelChoiceField(EmployeeModel.objects.all(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if ('instance' in kwargs) and (kwargs['instance'] is not None):
            self.fields['header_cathedra'].queryset = EmployeeModel.objects.filter(
                fk_cathedra=kwargs['instance'].id,
                rectorate_position__isnull=True,
                faculty_position__isnull=True,
                cathedra_position__isnull=True
            )


