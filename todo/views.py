from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from . models import Username, Password, Task
from django.urls import reverse


def home(request):
    return render(request, 'todo/home.html')


def login(request):
    return render(request, 'todo/login.html')


def logged_in(request):
    # if i can get the name, i can always get the tasks within it
    username = request.POST.get('Username')
    password = request.POST.get('Password')
    counter = 0
    try:
        for line in Username.objects.all():
            counter += 1
            if line.Username == username and line.password.all()[0].Password == password:
                return HttpResponseRedirect(reverse('todo:dashboard', args = (line.id,)))
            else:
                if counter == len(Username.objects.all()):
                    return render(request, 'todo/login.html',
                                  { 'error_message': 'Those values do not match anyone we have' })

    except ValueError:
        return render(request, 'todo/home.html', { 'error_message': 'Those values do not match anyone we have' })


def dashboard(request, user_id):
    username_object = get_object_or_404(Username, id = user_id)
    ordered = username_object.tasks.order_by('-time_created')

    return render(request, 'todo/dashboard.html', {
        'user_object': username_object,
        'tasks': ordered
    })


def add_task(request, user_id):
    try:
        task_name = request.POST.get('task_name')
        task_date = request.POST.get('task_date')
        task_date = task_date.replace('T', ' ')

        username_object = get_object_or_404(Username, id = user_id)
        username_object.tasks.create(task = task_name, time_to_do = task_date)
        return HttpResponseRedirect(reverse('todo:dashboard', args = (username_object.id,)))

    except ValidationError:
        return HttpResponseRedirect(reverse('todo:dashboard', args = (username_object.id,)))

def remove_task(request, user_id):
    # i need to know the user and task id
    posted = request.POST.get('line.id')
    username_object = get_object_or_404(Username, id = user_id)
    username_object.tasks.get(id = posted).delete()
    return HttpResponseRedirect(reverse('todo:dashboard', args = (username_object.id,)))




def signup(request):
    return render(request, 'todo/signup.html')


def signed_up(request):
    # this should take you to login
    # i need a way to notify people that the username they entered already exists
    username = request.POST.get('Username')
    password = request.POST.get('Password')

    # check if name exists
    for line in Username.objects.all():
        if username == line.Username:
            return HttpResponseRedirect(reverse('todo:signup_failed'))
    else:
        this_user = Username.objects.create(Username = username)
        this_user.password.create(Password = password)
        counter = 0
        try:
            for line in Username.objects.all():
                counter += 1
                if line.Username == username and line.password.all()[0].Password == password:
                    return HttpResponseRedirect(reverse('todo:dashboard', args = (line.id,)))
                else:
                    if counter == len(Username.objects.all()):
                        return render(request, 'todo/login.html',
                                      { 'error_message': 'Those values do not match anyone we have' })

        except ValueError:
            return render(request, 'todo/home.html', { 'error_message': 'Those values do not match anyone we have' })



def signup_failed(request):
    return render(request, 'todo/signup_failed.html')

