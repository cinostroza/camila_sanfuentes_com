from django.views.generic import TemplateView, ListView
from gallery.models import Gallery, GalleryImage


# Create your views here.
class GalleryIndex(TemplateView):
    template_name = 'gallery/index.html'


class GalleryView(ListView):
    context_object_name = 'gallery_list'
    template_name = 'gallery/gallery_index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = GalleryImage.objects.filter(gallery__title__iexact=self.kwargs['gallery_name'])
        context['galleries'] = Gallery.objects.all()
        return context

    def get_queryset(self):
        queryset = Gallery.objects.filter(title__iexact=self.kwargs['gallery_name'])
        return queryset
