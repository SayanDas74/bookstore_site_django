from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views import generic


class SignUpView(generic.CreateView):
    form_class    = UserCreationForm
    success_url   = reverse_lazy('login')
    template_name = 'signup.html'

from django.contrib.auth import logout

def logout_user(request):
  if request.user.is_authenticated:
    logout(request)
    return redirect('list')  
  return redirect('#')