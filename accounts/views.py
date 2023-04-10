from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView, ListView
from accounts.forms import LoginForm, CustomUserCreationForm
from accounts.models import Account


class LoginView(TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            messages.error(request, "Некорректные данные")
            return redirect('index_page')
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request, email=email, password=password)
        if not user:
            messages.warning(request, "Пользователь не найден")
            return redirect('index_page')
        login(request, user)
        messages.success(request, 'Добро пожаловать')
        next = request.GET.get('next')
        if next:
            return redirect(next)
        return redirect('main')


def logout_view(request):
    logout(request)
    return redirect('index_page')


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            login(request, user)
            return redirect(self.success_url)
        context = {'form': form}
        return self.render_to_response(context)


