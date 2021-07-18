from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from user.forms import CustomUserCreationForm
from user.forms import UserProfileForm


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect('home')
    else:
        form = CustomUserCreationForm()
        profile_form = UserProfileForm()

    return render(request, 'registration/signup.html', {'form': form, 'profile_form': profile_form})
