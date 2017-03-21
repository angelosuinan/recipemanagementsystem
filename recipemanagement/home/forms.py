from django import forms

class DataForm(forms.Form):
    data = forms.CharField(label='data', max_length=50)