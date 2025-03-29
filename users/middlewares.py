from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

first_lvl = "Работник"
second_lvl = "Администратор"
third_lvl = "Управляющий"
fourth_lvl = "Генеральный директор"

class DiplomaMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == "/register/" and request.method == "POST":
            diploma = str(request.POST.get("diploma"))
            if diploma == "Bachelor (Бакалавр)":
                request.lvl = first_lvl
                request.salary = 1000
            elif diploma == "Master (Магистратура)":
                request.lvl = second_lvl
                request.salary = 2000
            elif diploma == "Postgraduate (Аспирантура)":
                request.lvl = third_lvl
                request.salary = 3000
            elif diploma == "PhD (Кандидат наук)":
                request.lvl = fourth_lvl
                request.salary = 4000
            elif diploma == "None (Нету)":
                return HttpResponseBadRequest("Извините, вы не приняты, нужно наличие диплома")

        elif request.path == "/register/" and request.method == "GET":
            setattr(request, "lvl", "Уровень работы не определен")