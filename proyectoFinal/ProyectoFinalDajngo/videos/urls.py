from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.list_videos, name="list_videos"),
    path("upload/", views.upload_video, name="upload_video"),
    path("delete/<int:video_id>/", views.delete_video, name="delete_video"),
]