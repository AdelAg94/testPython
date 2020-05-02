from django.shortcuts import render,redirect
from django.http import HttpResponse
from myfirstapp.models import WebPage,Topic, AccessRecord
from .forms import ProfileInfo,NewUser,ExUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

def index(request):
    list_webpages = AccessRecord.objects.order_by('date')
    date_dict = {'access_records':list_webpages}
    return render(request, "myfirstapp/index.html",context = date_dict)

def test(request):
    return redirect('index')

def contactUs(request):
    msg = forms.Message()
    
    if request.method == "POST":
        msg = forms.Message(request.POST)
        
        # To see what the user sent on console/terminal you can add
        # forms.cleaned_data['name_of_attr'] to get what the user input 
        # in that attribute or (field) or (column) as the row input now
        if msg.is_valid():
            print("Name: " + msg.cleaned_data['name'])
            
    return render(request, "myfirstapp/contact_us.html", context = {'form' : msg})

def signup(request):

    registered = False

    if request.method == "POST":
        user_form = NewUser(request.POST)
        profile_form = ProfileInfo(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
               profile.profile_pic = request.FILES['profile_pic']
               profile.portfolio_url = request.POST['portfolio_url']
        
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = NewUser()
        profile_form = ProfileInfo()
    return render(request,"myfirstapp/sign_up.html",context={'registered':registered,
                                                            'user_form':user_form,
                                                            'profile_form':profile_form})

@login_required
def special(request):
    return HttpResponse("You are logged in")

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

def user_login(request):
    sent = False
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        sent = True
        user = authenticate(username=username , password = password)
        if user:
            if user.is_active:
                login(request,user)
                authn = True
                return redirect('index')
        else:
            authn = False
            
            user_form = ExUser()
            return render(request, 'myfirstapp/login.html', context = {'user_form':user_form,
                                                                        'authn':authn,
                                                                        'sent':sent,})
    else:
        user_form = ExUser()
        return render(request, 'myfirstapp/login.html', context = {'user_form':user_form})