from django.urls import path
from contact_manager.views import SubscribeView

app_name = 'contact_manager'

urlpatterns = [
    path('subscribe/', SubscribeView.as_view(), name='subscribe')
]
