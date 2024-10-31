from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import FormGastoView
app_name = 'app_core'

urlpatterns = [
    path('formulario', FormGastoView.as_view(), name='formulario')
] # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)