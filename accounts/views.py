from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'login.html')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')
@login_required
def profile_view(request):
    return render(request, 'profile.html')



def logout_view(request):
    logout(request)
    return redirect('login')
from django.contrib import messages

@login_required
def change_password_view(request):
    if request.method == "POST":
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if not request.user.check_password(old_password):
            messages.error(request, "Old password is incorrect")
        elif new_password != confirm_password:
            messages.error(request, "New passwords do not match")
        else:
            request.user.set_password(new_password)
            request.user.save()
            messages.success(request, "Password changed successfully")
            return redirect('login')

    return render(request, 'change_password.html')



# Create your views here.
