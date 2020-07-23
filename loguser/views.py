from django.shortcuts import render
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
        yr = request.POST.get('year')
        clg = request.POST.get('college')
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
    template_name = 'first.html'
    context = {'data' : 'meeting'}
    return render(request, template_name, context)

def display(request):
    data = Student.objects.filter(username='nsd')
    return render(request, 'show.html', {'data': data})