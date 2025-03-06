from django.urls import path
from .views import video_list, upload_video, custom_signup, custom_login, custom_logout, delete_video

urlpatterns = [
    path('',custom_login, name="custom_login"),
    path('videos/', video_list, name='video_list'),
    path('upload/', upload_video, name='upload_video'),
    path("signup/", custom_signup, name="custom_signup"),
    path("login/", custom_login, name="custom_login"),
    path("logout/", custom_logout, name="custom_logout"),
    path("delete/<int:video_id>/", delete_video, name="delete_video"),
]
