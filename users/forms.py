from random import choices
from django import forms
from django.contrib.auth.forms import UserCreationForm
from . import models


DIPLOMA = (
    ("None", "None"),
    ("Bachelor (Бакалавр)", "Bachelor (Бакалавр)"),
    ("Master (Магистратура)", "Master (Магистратура)"),
    ("Postgraduate (Аспирантура)", "Postgraduate (Аспирантура)"),
    ("PhD (Кандидат наук)", "PhD (Кандидат наук)")
)

GENDER = (
    ("Male", "Male"),
    ("Female", "Female"),
)

class CustomRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Укажите email")
    phone_number = forms.CharField(required=True, label="Укажите номер")
    age = forms.IntegerField(required=True, label="Укажите возраст")
    gender = forms.ChoiceField(choices=GENDER, required=True, label="Укажите пол")
    diploma = forms.ChoiceField(choices=DIPLOMA, required=True, label="Укажите ваш диплом")

    class Meta:
        model = models.CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "first_name",
            "last_name",
            "phone_number",
            "age",
            "gender",
            "diploma",
        )

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.phone_number = self.cleaned_data["phone_number"]
        user.age = self.cleaned_data["age"]
        user.gender = self.cleaned_data["gender"]
        user.diploma = self.cleaned_data["diploma"]

        if commit:
            user.save()
        return user