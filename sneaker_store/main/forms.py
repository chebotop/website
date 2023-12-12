from django import forms
from .models import ShoeModel

class ShoeModelForm(forms.ModelForm):
    extra_images = forms.FileField(
        required=False, 
        widget=forms.FileInput(attrs={'multiple': True})
    )

    class Meta:
        model = ShoeModel
        fields = '__all__'  # или перечислите нужные поля