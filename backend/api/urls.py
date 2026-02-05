from django.urls import path
from .views import upload_pdf, ask_pdf

urlpatterns = [
    path('pdf/upload/', upload_pdf, name='upload_pdf'),
    path('pdf/ask/', ask_pdf, name='ask_pdf'),
]