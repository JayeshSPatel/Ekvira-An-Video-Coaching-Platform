from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .forms import VideoUploadForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from allauth.account.forms import SignupForm, LoginForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Video


@login_required
def video_list(request):
    videos = Video.objects.filter(user=request.user)
    return render(request, 'videos/video_list.html', {'videos': videos})

@login_required
def upload_video(request):
    if request.method == "POST":
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save(commit=False)
            video.user = request.user
            video.save()
            return redirect('video_list')
    else:
        form = VideoUploadForm()
    return render(request, 'videos/upload_video.html', {'form': form})

# Custom Signup View
# def custom_signup(request):
#     if request.method == "POST":
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # Log in user after signup
#             return redirect("profile")  # Redirect to profile/dashboard
#     else:
#         form = SignupForm()
#     return render(request, "videos/signup.html", {"form": form})


def custom_signup(request):
    if request.method == "POST":
        # Fetching data from the form
        username = request.POST.get("username")
        email = request.POST.get("mail")
        password = request.POST.get("password")
        confirm_password = request.POST.get("re-enterpswd")

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return render(request, "users/signup.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return render(request, "videos/signup.html")

            # Create user
        user = User.objects.create_user(username=username, email=email, password=password)
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        # Automatically log the user in after signup
        login(request, user)
        return redirect("video_list")
    return render(request, "videos/signup.html")

# Custom Login View
def custom_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        form = AuthenticationForm(request, data={"username": username, "password": password})

        if form.is_valid():
            user = form.get_user()  # Get authenticated user
            login(request, user)
            return redirect("video_list")  # Redirect to profile/dashboard
    else:
        form = LoginForm()
    return render(request, "videos/login.html", {"form": form})

# Custom Logout View
def custom_logout(request):
    logout(request)
    return redirect("custom_login")  # Redirect to login page after logout

@login_required
def delete_video(request, video_id):
    video = get_object_or_404(Video, id=video_id)

    # Ensure only the video owner can delete it
    if request.user != video.user:
        return HttpResponseForbidden("You are not allowed to delete this video.")

    if request.method == "POST":
        video.delete()
        return redirect("video_list")  # Redirect to the video list after deletion

    return render(request, "videos/confirm_delete.html", {"video": video})
