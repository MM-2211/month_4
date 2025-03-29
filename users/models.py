from django.db import models
from django.contrib.auth.models import User

first_lvl = "Работник"
second_lvl = "Администратор"
third_lvl = "Управляющий"
fourth_lvl = "Генеральный директор"

class CustomUser(User):
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
    diploma = models.CharField(max_length=50, choices=DIPLOMA, default="None")
    phone_number = models.CharField(max_length=22)
    salary = models.PositiveIntegerField(blank=True, null=True)
    age = models.PositiveIntegerField(default=18)
    gender = models.CharField(choices=GENDER, max_length=10, default=first_lvl)
    lvl = models.CharField(max_length=100)


    def save(self, *args, **kwargs):
        if self.diploma == "Bachelor (Бакалавр)":
            self.lvl = first_lvl
            self.salary = 1000
        elif self.diploma == "Master (Магистратура)":
            self.lvl = second_lvl
            self.salary = 2000
        elif self.diploma == "Postgraduate (Аспирантура)":
            self.lvl = third_lvl
            self.salary = 3000
        elif self.diploma == "PhD (Кандидат наук)":
            self.lvl = fourth_lvl
            self.salary = 4000
        elif self.diploma == "None":
            self.lvl = "Извините, вы не приняты, нужно наличие диплома"
            self.salary = 0
        super().save(*args, **kwargs)
        
#
#
# class CustomUser(User):
#     DEGREE_CHOICES = (
#         ("bachelor", "Бакалавр"),
#         ("master", "Магистр"),
#         ("docent", "Доцент"),
#         ("none", "Без диплома"),
#     )
#
#     degree = models.CharField(max_length=20, choices=DEGREE_CHOICES, default="none")
#     position = models.CharField(max_length=100, blank=True, null=True)
#     salary = models.PositiveIntegerField(blank=True, null=True)
#     experience = models.PositiveIntegerField(default=0)
#     skills = models.TextField(blank=True)
#     languages = models.CharField(max_length=200, blank=True)
#     certifications = models.TextField(blank=True)
#     address = models.CharField(max_length=255, blank=True)
#     city = models.CharField(max_length=100, blank=True)
#     birth_date = models.DateField(null=True, blank=True)
#
#     def save(self, *args, **kwargs):
#         if self.degree == "bachelor":
#             self.position = "Библиотекарь"
#             self.salary = 50000
#         elif self.degree == "master":
#             self.position = "Главный библиотекарь"
#             self.salary = 70000
#         elif self.degree == "docent":
#             self.position = "Директор"
#             self.salary = 90000
#         else:
#             self.position = "Стажер"
#             self.salary = 30000
#
#         super().save(*args, **kwargs)