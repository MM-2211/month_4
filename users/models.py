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
