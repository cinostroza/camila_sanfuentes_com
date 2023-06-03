from django.views.generic import FormView, TemplateView
from django.contrib.auth import logout
from django.shortcuts import redirect

from camila_sanfuentes_com.models import MainPageContent
from contact_manager.models import ContactRequest
from contact_manager.forms import ContactForm
from django.urls import reverse_lazy
from django.contrib import messages

from gallery.models import Gallery, GalleryImage


class Index(FormView):
    form_class = ContactForm
    template_name = 'index_new.html'
    success_url = reverse_lazy('index')
    context_object_name = 'content'

    def form_valid(self, form):
        new_message = ContactRequest(
            email=form.data['email'],
            topic=form.data['topic'],
            message=form.data['message'],
        )
        new_message.save()
        messages.add_message(self.request, messages.INFO,
                             'Hemos recibido tu mensaje y te contactaremos a la brevedad!')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['content'] = MainPageContent.objects.first()
        context['galleries'] = Gallery.objects.all()
        context['carousel_images'] = GalleryImage.objects.filter(carousel_image=True).all()
        return context


class AboutMe(TemplateView):
    template_name = 'about_me.html'
    http_method_names = ['get']
    context_object_name = 'content'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['content'] = MainPageContent.objects.first()
        context['galleries'] = Gallery.objects.all()
        context['carousel_images'] = GalleryImage.objects.filter(carousel_image=True).all()
        return context


def logout_view(request):
    logout(request)
    return redirect('index')
