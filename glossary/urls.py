from django.urls import path, reverse_lazy
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', login_required(views.ArticleList.as_view(), login_url=reverse_lazy('login')), name="article_list"),
    path('create', views.ArticleCreate.as_view(), name="article_create"),
    path('update/<int:pk>', views.ArticleUpdate.as_view(), name="article_update"),
    path('view/<int:pk>', login_required(views.ArticleView.as_view(), login_url=reverse_lazy('login')), name="article_view"),
    path('delete/<int:pk>', views.ArticleDelete.as_view(), name="article_delete"),

]
