from django.urls import path
from .import views


urlpatterns = [
    path('content/', views.content_view, name='content'),
    path('audio-content/', views.view_audio_content, name='view_audio_content'),
    path('video-content/', views.view_video_content, name='view_video_content'),
    path('upload-audio/', views.upload_audio_view, name='upload_audio'),
    path('upload-video/', views.upload_video_view, name='upload_video'),
    path('emotion/', views.update_user_emotion, name='emotion'),
]
