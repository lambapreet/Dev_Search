from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUSerCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'