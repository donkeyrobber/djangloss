from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

# Create your views here.


class Signup(View):

    def get(self, request):

        form = UserCreationForm()

        return render(request, 'signup.html', {'form' : form})

    def post(self, request):

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                raw_password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=raw_password)
                login(request, user)
                return redirect('term_list')
        else:
            form = UserCreationForm()

        return render(request, 'signup.html', {'form': form})
