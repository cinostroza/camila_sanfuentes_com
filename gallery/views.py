from django.views.generic import TemplateView, ListView
from gallery.models import Gallery, GalleryImage


# Create your views here.
class GalleryIndex(TemplateView):
    template_name = 'gallery/index.html'


class MacroGallery(ListView):
    queryset = Gallery.objects.filter(title='Macrofotografía')
    context_object_name = 'gallery_list'
    template_name = 'gallery/gallery_index.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['images'] = GalleryImage.objects.filter(gallery__title='Macrofotografía')
        return context


class PaisajeGallery(ListView):
    queryset = Gallery.objects.filter(title='Paisajes')
    context_object_name = 'gallery_list'
    template_name = 'gallery/gallery_index.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['images'] = GalleryImage.objects.filter(gallery__title='Paisajes')
        return context


class FaunaGallery(ListView):
    queryset = Gallery.objects.filter(title='Fauna')
    context_object_name = 'gallery_list'
    template_name = 'gallery/gallery_index.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['images'] = GalleryImage.objects.filter(gallery__title='Fauna')
        return context


class BlackAndWhiteGallery(ListView):
    queryset = Gallery.objects.filter(title='Blanco y Negro')
    context_object_name = 'gallery_list'
    template_name = 'gallery/gallery_index.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['images'] = GalleryImage.objects.filter(gallery__title='Blanco y Negro')
        return context
