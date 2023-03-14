from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# this import not needed with class based as below - from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin #this is how to import login required and use the MIX IN functionality 
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)


class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

class LoginInterfaceView(LoginView):
    template_name = "home/login.html"


#implement typical view behavior 
class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today' : datetime.today()}


##below are function based views above is class based (class HomeView) these wo are doing the same thing but above offers more flexibility
##def home(request):
  ##  return render(request, 'home/welcome.html', {'today': datetime.today()})


#class is used to do the same thing as the def authorized below, however we still need to address @login_required
#LoginRequiredMixin must be before templateview
class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    extra_context = {'today' : datetime.today()}
    login_url = '/admin'

#@login_required(login_url='/admin')
#def authorized(request):
#    return render(request, 'home/authorized.html', {'today': datetime.today()})