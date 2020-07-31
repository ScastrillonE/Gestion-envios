from django.urls import path
from .views import save_notes

urlpatterns = [
    path('save/note/', save_notes, name='save_note'),
]
