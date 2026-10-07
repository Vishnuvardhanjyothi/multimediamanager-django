from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import youtube

def you(request):
    if request.method == 'POST':
        desc = request.POST.get('desc')
        image = request.FILES.get('img')
        video = request.FILES.get('vid')
        audio = request.FILES.get('audio')

        print("Description:", desc)
        print("Image:", image)
        print("Video:", video)
        print("Audio:", audio)

        youtube.objects.create(
            desc=desc,
            image=image,
            video=video,
            audio=audio
        )

    return render(request, 'media.html')


def media_all(request):
    obj = youtube.objects.all()
    return render(request, 'media_all.html', {'obj1': obj})


def update(request, id):

    obj = youtube.objects.get(id=id)

    if request.method == 'POST':

        obj.desc = request.POST.get('desc')

        if request.FILES.get('img'):
            obj.image = request.FILES.get('img')

        if request.FILES.get('vid'):
            obj.video = request.FILES.get('vid')

        if request.FILES.get('audio'):
            obj.audio = request.FILES.get('audio')

        obj.save()

        return redirect('media')

    return render(request, 'update.html', {'obj': obj})

def delmedia(request,id):
    obj = youtube.objects.get(id=id)
    obj.delete()
    return redirect('media')

def single_media(request, id):
    obj = youtube.objects.get(id=id)
    return render(request, 'single_media.html', {'obj': obj})
