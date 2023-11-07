from django import forms
from .models import RailwaySystem, Railway, Train

class RailwaySystemForm(forms.ModelForm):
    class Meta:
        model = RailwaySystem
        fields = '__all__'

class RailwayForm(forms.ModelForm):
    class Meta:
        model = Railway
        fields = '__all__'

class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = '__all__'
