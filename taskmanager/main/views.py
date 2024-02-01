from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template

from .models import Task
from .forms import TaskForm, ContactForm
from django.forms import forms


def index(request):
    tasks = Task.objects.order_by("-id")
    return render(request, 'main/index.html', {'title': 'Home', 'tasks': tasks})

def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ""
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Invalid form"

    form  = TaskForm()
    context = {
        'form': form
    }
    return render(request, 'main/create.html', context)



def contacts(request):
    context = {}
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['message'])
            context = {'succsess': 1}
            return redirect('home')
    else:
        form = ContactForm()
    context['form'] = form

    return render(request, 'main/contacts.html', context=context)




def send_message(name, email, message):
    text = get_template('message.html')
    html = get_template('message.html')
    context = {'name': name, 'email': email, 'message': message}
    subject = "Message from user"
    from_email = "from@example.com"
    text_content = text.render(context)
    html_content = html.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, ['admin@example.com'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()


