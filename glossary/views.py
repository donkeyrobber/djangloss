from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . import models


class ArticleList(ListView):
    model = models.Term
    template_name = 'article/article_list.html'


class ArticleView(DetailView):
    model = models.Term
    template_name = 'article/article_detail.html'


class ArticleCreate(CreateView):
    model = models.Term
    fields = ['term', 'description']
    template_name = 'article/article_form.html'
    success_url = reverse_lazy('article_list')

    def form_valid(self, form):
        term = form.save(commit=False)
        term.created_by = self.request.user
        term.save()
        return redirect(reverse_lazy('article_list'))


class ArticleUpdate(UpdateView):
    model = models.Term
    fields = ['term', 'description']
    template_name = 'article/article_form.html'
    success_url = reverse_lazy('article_list')


class ArticleDelete(DeleteView):
    model = models.Term
    template_name = 'article/article_confirm_delete.html'
    success_url = reverse_lazy('article_list')