from django.views.generic import FormView
from contact_manager.forms import SubscribeForm


# Create your views here.

class SubscribeView(FormView):
    form_class = SubscribeForm
    template_name = 'index.html'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
