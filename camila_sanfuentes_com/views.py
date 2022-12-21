from django.views.generic import FormView
from django.contrib.auth import logout
from django.shortcuts import redirect

from camila_sanfuentes_com.models import MainPageContent
from contact_manager.models import Subscriber
from contact_manager.forms import SubscribeForm
from django.urls import reverse_lazy
from django.contrib import messages


class Index(FormView):
    form_class = SubscribeForm
    template_name = 'index.html'
    success_url = reverse_lazy('index')
    context_object_name = 'content'

    def form_valid(self, form):
        new_sub = Subscriber(email=form.data['email'])
        new_sub.save()
        messages.add_message(self.request, messages.INFO,
                             'Se ha registrado tu correo existosamente!. Pronto recibiras actualizaciones.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['content'] = MainPageContent.objects.first()
        return context

def logout_view(request):
    logout(request)
    return redirect('index')
