from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import FormView
from .forms import ContactForm

from .models import *


class Products_List(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'shop.html'


class Home(ListView):
    model = Home
    context_object_name = 'homepage'
    template_name = 'home.html'


class Userlist(ListView):
    model = Person
    context_object_name = 'users'
    template_name = 'user_list.html'


from django.shortcuts import render, redirect
from .forms import SignupForm
from .models import Registered_user
from django.contrib.auth.hashers import make_password, check_password


class RegisterView(FormView):
    template_name = 'register.html'
    form_class = SignupForm
    success_url = '/login'

    def form_valid(self, form):
        user = form.save(commit=False)
        user.password = make_password(user.password)
        user.save()
        return super().form_valid(form)


class LoginView(View):
    template_name = 'login.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = Registered_user.objects.get(username=username)
            if check_password(password, user.password):
                request.session['user_id'] = user.id
                return redirect('home')
            else:
                return render(request, self.template_name, {'error': 'Invalid password'})
        except Registered_user.DoesNotExist:
            return render(request, self.template_name, {'error': 'User does not exist'})


class LogoutView(View):
    def get(self, request):
        if 'user_id' in request.session:
            del request.session['user_id']
        return redirect('login')


class About(ListView):
    model = About
    context_object_name = 'about'
    template_name = 'about.html'


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'contact.html', context=context)
