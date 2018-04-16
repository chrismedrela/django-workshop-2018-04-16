from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail


def register(request, template_name='userauth/register.html', next_page_name='/'):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                'A new user has registered',
                'Here is the message',
                'from@email.com',
                ['your@email.com'],
                fail_silently=False,
            )
            return HttpResponseRedirect(reverse(next_page_name))
    else:
        form = UserCreationForm()
    return render(request, template_name, {'form': form})