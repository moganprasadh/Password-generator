# generator/forms.py
from django import forms

class PasswordForm(forms.Form):
    include_uppercase = forms.BooleanField(required=False, label='Include uppercase letters')
    include_numbers = forms.BooleanField(required=False, label='Include numbers')
    include_special = forms.BooleanField(required=False, label='Include special symbols')
    length = forms.IntegerField(min_value=4, max_value=50, initial=12, label='Password length')
