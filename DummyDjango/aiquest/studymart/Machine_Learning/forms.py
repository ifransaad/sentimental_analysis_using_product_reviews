from django import forms

class UserInput(forms.Form):
    write_Review = forms.CharField("Write your Review")