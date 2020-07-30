from django import template
from django.core.paginator import Paginator

from notes.models import Note

register = template.Library()

@register.inclusion_tag('notes/notes.html')
def notes_list(request):
    if request.method =='GET':
        notes = Note.objects.all()
        paginator = Paginator(notes,6)
        page = request.GET.get('page')
        notes = paginator.get_page(page)
        return {
            'notes': notes
        }