from django import forms
from .models import Grower, Plant, SurveillanceRecord

class GrowerForm(forms.ModelForm):
    class Meta:
        model = Grower
        fields = ['name', 'email', 'property_location']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input mt-1 block w-full'}),
            'email': forms.EmailInput(attrs={'class': 'form-input mt-1 block w-full'}),
            'property_location': forms.TextInput(attrs={'class': 'form-input mt-1 block w-full'}),
        }

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['grower', 'plant_type', 'location', 'planting_date']
        widgets = {
            'grower': forms.Select(attrs={'class': 'form-select mt-1 block w-full'}),
            'plant_type': forms.TextInput(attrs={'class': 'form-input mt-1 block w-full'}),
            'location': forms.TextInput(attrs={'class': 'form-input mt-1 block w-full'}),
            'planting_date': forms.DateInput(attrs={'class': 'form-input mt-1 block w-full', 'type': 'date'}),
        }

class SurveillanceRecordForm(forms.ModelForm):
    class Meta:
        model = SurveillanceRecord
        fields = ['plant', 'surveillance_date', 'pest_or_disease', 'plant_part', 'severity', 'notes']
        widgets = {
            'plant': forms.Select(attrs={'class': 'form-select mt-1 block w-full'}),
            'surveillance_date': forms.DateTimeInput(attrs={'class': 'form-input mt-1 block w-full', 'type': 'datetime-local'}),
            'pest_or_disease': forms.TextInput(attrs={'class': 'form-input mt-1 block w-full'}),
            'plant_part': forms.Select(attrs={'class': 'form-select mt-1 block w-full'}),
            'severity': forms.Select(attrs={'class': 'form-select mt-1 block w-full'}),
            'notes': forms.Textarea(attrs={'class': 'form-textarea mt-1 block w-full', 'rows': 4}),
        }