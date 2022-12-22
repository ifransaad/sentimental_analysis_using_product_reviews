from django import forms

class UserInput(forms.Form):
    input_string = forms.CharField()