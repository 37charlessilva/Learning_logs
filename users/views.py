from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Faz o cadastro de um novo usuário."""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()

            authenticated_user = authenticate(
                request,
                username=new_user.username,
                password=request.POST['password1']
            )

            login(request, authenticated_user)
            return redirect('learning_logs:index')

    context = {'form': form}
    return render(request, 'users/register.html', context)