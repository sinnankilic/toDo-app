from django import forms

from .models import toDoModel


class toDoForm(forms.ModelForm):

      class Meta:
            model=toDoModel
            fields="__all__"
            exclude = ['completed',]
            labels = {
                  'title': 'Başlık',
                  'details': 'Açıklamalar',
                  'completed': 'Tamamlandı mı?',
                  'importance': 'Önem Derecesi'
            }


            widgets={
                  'title':forms.TextInput(attrs={'class':'form-control','placeholder':'görev'}),
                  'details':forms.Textarea(attrs={'class':'form-control','rows':4,'placeholder':'detay'}),
                  'completed':forms.CheckboxInput(attrs={'class':'form-check-input'}),
                  'importance':forms.Select(attrs={'class':'form-select'}),
            }
            