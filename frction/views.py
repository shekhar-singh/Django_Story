from django.shortcuts import render,render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
    if request.user.is_authenticated():
        print request. user.username
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return render_to_response('frction/home.html')

def login(request):
    if request.user.is_authenticated():
        #print request. user.username
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        c = {}
        c.update(csrf(request))
        return render_to_response('frction/login.html',c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request,user)
        return HttpResponseRedirect('/accounts/loggedin/')
    else:
        return HttpResponseRedirect('/accounts/invalid/')

@login_required
def loggedin(request):
    author = request.user.username
    return render(request,'frction/loggedin.html', {'author':author})

def invalid_login(request):
    return render_to_response('frction/invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('frction/logout.html')

def register_user(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/accounts/success/')
            else:
                return render(request,'frction/register.html', {'form':form })
        args = {}
        args.update(csrf(request))

        args['form'] = UserCreationForm()
        return render_to_response('frction/register.html', args)


def success(request):
    return render_to_response('frction/success.html')