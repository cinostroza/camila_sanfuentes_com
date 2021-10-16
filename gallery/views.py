from django.views.generic import TemplateView


# Create your views here.
class GalleryIndex(TemplateView):
    template_name = 'gallery/index.html'
