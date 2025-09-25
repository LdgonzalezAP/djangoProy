from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Video
from .forms import VideoForm

@login_required
def list_videos(request):
    videos = Video.objects.filter(usuario=request.user)
    return render(request, "videos/list.html", {"videos": videos})

@login_required
def upload_video(request):
    if request.method == "POST":
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(usuario=request.user)
            return redirect("list_videos")
    else:
        form = VideoForm()
    return render(request, "videos/upload_video.html", {"form": form})

@login_required
def delete_video(request, video_id):
    video = get_object_or_404(Video, id=video_id, usuario=request.user)
    if request.method == "POST":
        video.delete()
        return redirect("list_videos")
    return render(request, "videos/delete_videos.html", {"video": video})