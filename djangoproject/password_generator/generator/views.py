# generator/views.py
import random
import string
from django.shortcuts import render
from .forms import PasswordForm

def generate_password(length, include_uppercase, include_numbers, include_special):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def home(request):
    password = ''
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            length = form.cleaned_data['length']
            include_uppercase = form.cleaned_data['include_uppercase']
            include_numbers = form.cleaned_data['include_numbers']
            include_special = form.cleaned_data['include_special']
            password = generate_password(length, include_uppercase, include_numbers, include_special)
    else:
        form = PasswordForm()

    return render(request, 'generator/home.html', {'form': form, 'password': password})
