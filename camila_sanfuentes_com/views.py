from django.views.generic import TemplateView, FormView
from django.contrib.auth import logout
from django.shortcuts import redirect
from contact_manager.models import Subscriber
from contact_manager.forms import SubscribeForm
from django.urls import reverse_lazy


class Index(FormView):
    form_class = SubscribeForm
    template_name = 'index.html'
    success_url = '/'

    def form_valid(self, form):
        new_sub = Subscriber(email=form.data['email'])
        new_sub.save()
        return super().form_valid(form)


def logout_view(request):
    logout(request)
    return redirect('index')
