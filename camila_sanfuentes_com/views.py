from django.views.generic import TemplateView
from django.contrib.auth import logout
from django.shortcuts import redirect

class Index(TemplateView):
    template_name = 'index.html'


def logout_view(request):
    logout(request)
    return redirect('index')