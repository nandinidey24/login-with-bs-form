from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import LoginForm
from .models import Student

# Create your views here.
def action(request):
    form = LoginForm(data=request.POST or None)
    if form.is_valid():
        uname = form.cleaned_data['email']
        fname = form.cleaned_data['firstname']
        lname = form.cleaned_data['lastname']
        password = form.cleaned_data['password']
        cred = User.objects.create(
            username = uname,
            email = uname,
            first_name = fname,
            last_name = lname,
        )
        cred.set_password("password")
        cred.save()
        yr = form.cleaned_data['year']
        clg = form.cleaned_data['college']
        obj = Student.objects.create(
            username = uname,
            email = uname,
            firstname = fname,
            lastname = lname,
            year = yr,
            college = clg
        )
        obj.set_password("password")
        obj.save()
        form = LoginForm(request.POST or None)
    template_name = 'index.html'
    context = {'form' : form}
    return render(request, template_name, context)

def loguser(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username = username, password = password)
    if user is not None:
        login(request, user)
        print('User verified')
        print(request.user.username)
        return redirect("show")
    else:
        print('No such user')
    template_name = 'login.html'
    context = {'data' : 'meeting'}
    return render(request, template_name, context)

def log_out(request):
    logout(request)
    return redirect("")

def data(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        test = User.objects.create(
            username = email,
            first_name = fname,
            last_name = lname,
            email = email,
        )
        test.set_password(request.POST.get('password'))
        test.save()
        yr = request.POST.get('yr')
        clg = request.POST.get('clg')
        pw = request.POST.get('password')
        obj1 = Student.objects.create(
            username = email,
            firstname = fname,
            lastname = lname,
            email = email,
            year = yr,
            college = clg,
            password = pw
        )
        obj1.save()
    template_name = 'signup.html'
    context = {'data' : 'meeting'}
    return render(request, template_name, context)

@login_required
def display(request):
    data = Student.objects.filter(username=request.user.username)
    return render(request, 'show.html', {'data': data})