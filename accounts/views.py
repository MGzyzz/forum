from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import views, login
from django.urls import reverse_lazy, reverse
from django.contrib.auth import views, login, get_user_model, update_session_auth_hash
from accounts.forms import LoginForm, RegisterForm
from django.views.generic import CreateView, DetailView
from accounts.models import User, Profile

# Create your views here.
class AuthSuccessUrlMixin:
    def get_success_url(self):

        next_url = self.request.GET.get('next')

        if not next_url:
            next_url = self.request.POST.get('next')

        if not next_url:
            next_url = reverse('home')

        return next_url


class Logout(views.LogoutView):
    def get_next_page(self):
        return self.request.META.get('HTTP_REFERER')


class LoginView(AuthSuccessUrlMixin, views.LoginView):
    template_name = 'login.html'
    form_class = LoginForm


class RegisterView(CreateView):
    model = User
    template_name = 'register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        user = form.save()

        avatar_file = self.request.FILES.get('avatar')
        password = form.cleaned_data.get('password1')
        user.set_password(password)
        user.save()
        if avatar_file:
            profile = Profile.objects.get_or_create(user=user)[0]
            profile.avatar = avatar_file
            profile.save()

        login(self.request, user)
        return redirect('home')


class Detail(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'user/detail.html'
    context_object_name = 'user'
    pk_url_kwarg = 'id'
    paginate_related_by = 5
    paginate_related_orphans = 0