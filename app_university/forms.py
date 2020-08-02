from app_university import models
from django import forms

class RectoratePositionForm(forms.ModelForm):

    position_title = forms.CharField(max_length=70, label='Должность')
    belong_id = forms.ChoiceField(choices=(), required=True, label='В подчинении у')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)  
        r = models.RectoratePosition.objects.all()
        self.choices = []
        if(not len(r)):
            newPosition = models.RectoratePosition(position_title="без подчинения", belong_id=0)
            newPosition.save()
            self.fields['belong_id'].choices = [(0, "без подчинения")]
        else:
            for item in r:
                self.choices.append((item.id, item.position_title))
                self.fields['belong_id'].choices = self.choices