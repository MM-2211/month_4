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
#
#
# DEGREE_CHOICES = (
#         ("bachelor", "Бакалавр"),
#         ("master", "Магистр"),
#         ("docent", "Доцент"),
#         ("none", "Без диплома"),
#     )
#
# class CustomRegisterForm(UserCreationForm):
#     degree = forms.ChoiceField(choices=DEGREE_CHOICES, required=True, label="Ваш диплом")
#     experience = forms.IntegerField(required=True, label="Опыт работы")
#     skills = forms.CharField(widget=forms.Textarea, required=False, label="Навыки")
#     languages = forms.CharField(required=False, label="Знание языков")
#     certifications = forms.CharField(widget=forms.Textarea, required=False, label="Сертификаты")
#     address = forms.CharField(required=True, label="Адрес")
#     city = forms.CharField(required=True, label="Город")
#     birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=True, label="Дата рождения")
#
#     class Meta:
#         model = models.CustomUser
#         fields = (
#             'username',
#             'password1',
#             'password2',
#             'first_name',
#             'last_name',
#             'degree',
#             'experience',
#             'skills',
#             'languages',
#             'certifications',
#             'address',
#             'city',
#             'birth_date'
#         )
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.degree = self.cleaned_data['degree']
#         user.experience = self.cleaned_data['experience']
#         user.skills = self.cleaned_data['skills']
#         user.languages = self.cleaned_data['languages']
#         user.birth_date = self.cleaned_data['birth_date']
#         user.certifications = self.cleaned_data['certifications']
#         user.address = self.cleaned_data['address']
#         user.city = self.cleaned_data['city']
#
#         if commit:
#             user.save()
#         return user