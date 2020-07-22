from django.shortcuts import render, redirect
from django.http import HttpResponse
from inventory.models import Artist, Album
from inventory.forms import AlbumForm, ArtistForm
# Create your views here.

def index(request):
    artists = Artist.objects.all()
    return render(request, "inventory/index.html", locals())

def album_new(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.save()
        return redirect('index')
    else:
        form = AlbumForm()
        heading = "Album"
        return render(request, 'inventory/new.html', locals())

def artist_new(request):
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            artist = form.save(commit=False)
            artist.save()
        return redirect('index')
    else:
        form = ArtistForm()
        heading = "Artist"
        return render(request, 'inventory/new.html', locals())
