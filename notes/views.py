from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Note
# Create your views here.

@csrf_exempt
def save_notes(request,id=None):

    if request.method == 'GET':
        print('ACAAA')
        note = Note.objects.get(id=id)
        if note:
            context = {
                'title_note': note.title,
                'content_note':note.content,
                'status':note.status,
            }
            return JsonResponse(context)


    if request.method == 'POST':
        if request.is_ajax():
            data = {}
            title = request.POST['title_note']
            content = request.POST['content_note']
            user = request.user
            try:
                if request.POST['status']:
                    status = True
            except:
                status = False

            note = Note(
                user=user,
                title= title,
                content = content,
                status= status,
            )

            if note.status == True:
                data['success'] = 'La nota no fue agregada'
            else:
                note.save()
                data['success'] = 'Nota creada'



            return JsonResponse(data)