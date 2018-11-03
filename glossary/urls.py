from django.urls import path

from . import views

urlpatterns = [
    path('', views.TermList.as_view(), name="term_list"),
    path('create', views.TermCreate.as_view(), name="term_create"),
    path('update/<int:pk>', views.TermUpdate.as_view(), name="term_update"),
    path('view/<int:pk>', views.TermView.as_view(), name="term_view"),
    path('delete/<int:pk>', views.TermDelete.as_view(), name="term_delete"),

]
