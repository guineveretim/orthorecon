from django import forms
from .models import Referral

class ReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = ['patient_name', 'patient_age', 'diagnosis', 'urgency', 'xray_link', 'doctor_name', 'practice', 'doctor_contact']
        widgets = {
            'patient_name': forms.TextInput(attrs={'placeholder': 'Patient full name'}),
            'patient_age': forms.NumberInput(attrs={'placeholder': 'Age'}),
            'diagnosis': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Diagnosis / problem'}),
            'xray_link': forms.URLInput(attrs={'placeholder': 'Paste Google Drive / X-ray link (optional)'}),
            'doctor_name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'practice': forms.TextInput(attrs={'placeholder': 'Practice / Hospital'}),
            'doctor_contact': forms.TextInput(attrs={'placeholder': 'Your phone / email'}),
        }