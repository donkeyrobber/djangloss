from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('', login_required(views.ArticleList.as_view()), name="article_list"),
    path('create', views.ArticleCreate.as_view(), name="article_create"),
    path('update/<int:pk>', views.ArticleUpdate.as_view(), name="article_update"),
    path('view/<int:pk>', views.ArticleView.as_view(), name="article_view"),
    path('delete/<int:pk>', views.ArticleDelete.as_view(), name="article_delete"),

]
