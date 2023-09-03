from django.shortcuts import render
from googleapiclient.discovery import build
from django.conf import settings
from .models import  Dersler, KullaniciBegeni,Yorum
from django.contrib.auth.decorators import login_required
from django.db.models import F
from .forums import YorumForm
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Dersler, KullaniciBegeni
# Create your views here.

def temel_mantik(request):
    return render(request,"dersler/temel_mantik.html")


def geometri(request):
    return render(request,"dersler/geometri.html")

def hakkimizda(request):
    return render(request,"dersler/hakkimizda.html")

def iletisim(request):
    return render(request,"dersler/iletisim.html")




def get_channel_videos(channel_id):
    youtube = build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)
    response = youtube.search().list(
        part='snippet',
        channelId=channel_id,
        type='video',
        order='date',
        maxResults=10
    ).execute()

    videos = response['items']
     # Veritabanına videoları kaydetme
     # Veritabanına videoları kaydetme
    for video in videos:
        video_id = video['id']['videoId']
        title = video['snippet']['title']
        description = video['snippet']['description']
        lesson, created = Dersler.objects.get_or_create(video_id=video_id, defaults={'title': title, 'description': description})

  
    return videos

def get_channel_live_videos(channel_id):
    youtube = build('youtube', 'v3', developerKey=settings.YOUTUBE_API_KEY)
    response = youtube.search().list(
        part='snippet',
        channelId=channel_id,
        eventType='live',
        type='video',
        order='date',
        maxResults=10
    ).execute()
   
    videos = response['items']

      # Veritabanına videoları kaydetme
    for video in videos:
        print('DERSLER',video)
        video_id = video['id']['videoId']
        title = video['snippet']['title']
        description = video['snippet']['description']
        lesson = Dersler.objects.create(video_id=video_id, title=title, description=description)
    

  
    return videos

def matematik(request):
    dersler = Dersler.objects.filter(is_active=True)
    context={
        'dersler':dersler
    }
    return render(request, 'dersler/matematik.html', context)



@login_required
def matematik_detay(request, video_id):
    ders = get_object_or_404(Dersler, video_id=video_id)

    if request.method == 'POST' and 'begeni_artir' in request.POST:
        kullanici = request.user
        if not KullaniciBegeni.objects.filter(kullanici=kullanici, ders=ders).exists():
            ders.begeni_sayisi = F('begeni_sayisi') + 1
            ders.save()
            KullaniciBegeni.objects.create(kullanici=kullanici, ders=ders)

            # AJAX isteği geldiğinde beğeni sayısını döndür

            return JsonResponse({'begeni_sayisi': ders.begeni_sayisi})
    yorumlar = Yorum.objects.filter(ders=ders).order_by('-tarih')
    yorum_form = YorumForm()

    if request.method == 'POST' and 'yorum_yap' in request.POST:
        yorum_form = YorumForm(request.POST)
        if yorum_form.is_valid():
            yorum = yorum_form.save(commit=False)
            yorum.kullanici = request.user
            yorum.ders = ders
            yorum.save()
            yorum_form = YorumForm()

    context = {
        'ders': ders,
        'yorumlar': yorumlar,
        'yorum_form': yorum_form,
    }
    return render(request, 'dersler/matematik_detay.html', context)

def youtube_live(request):
    channel_id = 'UCw9LDzAA2KsXyVKzNmHmt6g'  # Belirli bir kanalın kimliği
    live_videos = get_channel_live_videos(channel_id)
    context = {
        'live_videos': live_videos
    }
    return render(request, 'dersler/youtube_live.html', context)


def dersler_search(request):
    arama_terimi = request.GET.get('q')
    dersler = Dersler.objects.filter(title__icontains=arama_terimi)
    return render(request, 'dersler/dersler_search.html', {'dersler': dersler, 'arama_terimi': arama_terimi})


@login_required
def begenilen_videolar(request):
    # Kullanıcının beğendiği videoları al
    liked_videos = KullaniciBegeni.objects.filter(kullanici=request.user)

    context = {'liked_videos': liked_videos}
    return render(request, 'dersler/liked_lessons.html', context)
