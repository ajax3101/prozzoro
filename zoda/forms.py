from django import forms
from .models import Region, Agency

class TenderFilterForm(forms.Form):
    region = forms.ModelChoiceField(queryset=Region.objects.all(), empty_label="Усі регіони", required=False, label="Регіон:", widget=forms.Select(attrs={'class': 'form-control'}))
    agency = forms.ModelChoiceField(queryset=Agency.objects.all(), empty_label="Усі установи", required=False, label="Установа:", widget=forms.Select(attrs={'class': 'form-control'}))
