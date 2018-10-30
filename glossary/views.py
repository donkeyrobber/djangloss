from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . import models


class TermList(ListView):
    model = models.Term
    template_name = 'terms/term_list.html'


class TermView(DetailView):
    model = models.Term
    template_name = 'terms/term_detail.html'


class TermCreate(CreateView):
    model = models.Term
    fields = ['term', 'description']
    template_name = 'terms/term_form.html'
    success_url = reverse_lazy('term_list')


class TermUpdate(UpdateView):
    model = models.Term
    fields = ['term', 'description']
    template_name = 'terms/term_form.html'
    success_url = reverse_lazy('term_list')


class TermDelete(DeleteView):
    model = models.Term
    template_name = 'terms/term_confirm_delete.html'
    success_url = reverse_lazy('term_list')