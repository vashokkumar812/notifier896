from django.shortcuts import render
from django.template import loader
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .models import post,comment
from .forms import postform,commentform
def index(request):
    if request.method == 'POST':
        form = postform(request.POST or None)       
    # check if form data is valid 
        ano = post(name=request.POST['name'])# save the form data to model 
        ano.save() 
    form = postform()  
    posts = post.objects.all()
    context={"posts" : posts,"me" : request.user}
    
    return render(request, "comments/index.html", context)
    
def room(request, room_name):
    currentpost = post.objects.get(pk=room_name)
    if request.method == 'POST':
        form = commentform(request.POST or None)       
    # check if form data is valid 
        ano = comment(name=request.POST['name'],by = request.user, of = currentpost)# save the form data to model 
        ano.save() 
    form = commentform()  
    context={}
    print(request.user.pk)
    return render(request, 'comments/room.html', {
        'room_name': room_name,
        'currentuser' : request.user
    })
    
def signin(request,username):
        user = authenticate(username=username, password=username)
        login(request, user)   
        return HttpResponseRedirect('/')