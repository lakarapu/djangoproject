from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account is created! You can login now')
            return redirect('Login')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile(user=request.user)
    if request.method == 'POST':
        uu_form = UserUpdateForm(request.POST, instance=request.user)
        pu_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if uu_form.is_valid() and pu_form.is_valid():
            uu_form.save()
            pu_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile')
    else:
        uu_form = UserUpdateForm(request.POST, instance=request.user)
        pu_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

    context ={
        'uu_form': uu_form,
        'pu_form': pu_form
        }

    return render(request, 'users/profile.html', context)