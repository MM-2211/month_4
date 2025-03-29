from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.http import HttpResponse
from django.views import generic

from .models import Basket

class SearchBasketView(generic.ListView):
    template_name = 'basket/basket_list.html'
    context_object_name = 'basket'

    def get_queryset(self):
        return models.Basket.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context

class CreateBasket(generic.CreateView):
    template_name = 'basket/create_basket.html'
    form_class = forms.BasketForm
    success_url = "/basket_list/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateBasket, self).form_valid(form=form)



class BasketListView(generic.ListView):
    template_name = 'basket/basket_list.html'
    context_object_name = 'basket'
    model = models.Basket

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

class BasketDetailView(generic.DetailView):
    template_name = 'basket/basket_detail.html'
    context_object_name = 'basket_id'

    def get_object(self, *args, **kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(models.Basket, id=basket_id)


class BasketUpdateView(generic.UpdateView):
    template_name = 'basket/basket_update.html'
    form_class = forms.BasketForm
    success_url = "/basket_list/"

    def get_object(self, *args, **kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(models.Basket, id=basket_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BasketUpdateView, self).form_valid(form=form)



class BasketDeleteView(generic.DeleteView):
    template_name = 'basket/confirm_delete.html'
    success_url = "/basket_list/"

    def get_object(self, *args, **kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(models.Basket, id=basket_id)


