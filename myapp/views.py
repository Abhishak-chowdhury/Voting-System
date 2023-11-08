from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from myapp.models import *
from django.contrib import messages
from django.db.models import Count
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate,login as login_details,logout as logout_details
import random
import string
from datetime import date
# Create your views here.
def home(request):
    return render(request,'index.html')
@login_required(login_url='user-login')
def user_home(request,user1):
    user_object=UserDetails.objects.get(user__username=user1)
    contex={'user_object':user_object}
    return render(request,'user-dashboard.html',contex)
@login_required(login_url='admin-login')
def admin_home(request):
    return render(request,'admin-dashboard.html')
def user_login(request):
    if request.method == 'POST':
        Email = request.POST.get('email')
        Password = request.POST.get('password')
        try:
            obj = User.objects.get(email=Email)
        
            username=obj.username
            print(username)
            user = authenticate(request,email = Email ,password = Password,username=username)
            print(user)
            if user is not None:
                login_details(request, user)
                
                messages.success(request,f"sucessfully registered {Email}")
                return redirect('user-dashboard',user1=request.user)
            else:
                messages.warning(request,"password is incorrect")
                return redirect('user-login')
        except Exception as e:
            print(e)
            messages.warning(request,"login details are incorrect")
            return redirect('user-login')
    
    return render(request,'user-login.html')
def user_register(request):
    if request.method == 'POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        ph=request.POST.get('ph')
        zip=request.POST.get('zip')
        city=request.POST.get('city')
        gender=request.POST.get('gender')
        address=request.POST.get('address')
        vcard_number=request.POST.get('vcard_number')
        p_img=request.FILES['p_img']
        v_img=request.FILES['v_img']
        password=request.POST.get('password')
        repassword=request.POST.get('re-password')
        if User.objects.filter(email=email).exists():
            messages.warning(request,'email has already exists,to continue login')
            return redirect('user-register')
        else:
            if password == repassword:
                N = 5
                res = ''.join(random.choices(string.ascii_lowercase +string.digits, k=N))
                use=User.objects.create(username=firstname+'_'+res,first_name=firstname,last_name=lastname,email=email)
                use.set_password(password)
                use.save()
                obj = User.objects.get(email=email)
        
                username=obj.username
                print(username)
                user = authenticate(request,email = email ,password = password,username=username)
                if user is not None:
                    login_details(request, user)
                # user_obj=User.objects.get(username=request.user)
                    user_obj=UserDetails.objects.create(user=request.user,phone_number=ph,zip=zip,city=city,address=address,gender=gender,voter_number=vcard_number)
                    user_obj.profile_img=p_img
                    user_obj.voter_img=v_img
                    user_obj.save()
                    messages.success(request,'you are registered successfully and login to continue')
                    return redirect('user-register')
            else:
                messages.warning(request,'re-entered password does not matched ')
                return redirect('user-register')
    return render(request,'user-register.html')
def admin_login(request):
    if request.method == 'POST':
        Email = request.POST.get('email')
        Password = request.POST.get('password')
        try:
            obj = User.objects.get(email=Email,is_superuser=True)
        
            username=obj.username
            print(username)
            user = authenticate(request,email = Email ,password = Password,username=username)
            print(user)
            if user is not None:
                login_details(request, user)
                
                messages.success(request,f"sucessfully registered {Email}")
                return redirect('admin-dashboard')
            else:
                messages.warning(request,"password is incorrect")
                return redirect('admin-login')
        except Exception as e:
            print(e)
            messages.warning(request,"you are not eligable to login in admin site")
            return redirect('admin-login')
    return render(request,'admin-login.html')

def logout(request):
    logout_details(request)
    messages.success(request,'thank you for spending some moments')
    return redirect('user-login')
def Admin_logout(request):
    logout_details(request)
    messages.success(request,'thank you for spending some moments')
    return redirect('admin-login')
@login_required(login_url='admin-login')
def view_voters(request):
    voters=UserDetails.objects.all().order_by('-id')
    contex={
        'voters':voters
    }
    return render(request,'view-voters.html',contex)
@login_required(login_url='admin-login')
def Activate_Voter(request):
    if request.method == 'POST':
        user_id=request.POST.get('user_id')
        user_oj=UserDetails.objects.get(id=user_id)
        user_oj.status=True
        user_oj.save()
        return redirect('view-voters')
@login_required(login_url='admin-login')
def Add_Election(request):
    elections=AvailableElection.objects.all().order_by('-id')
    today = date.today()
    contex={
        'elections':elections,
        'today':today
    }
    if request.method == 'POST':
        electionname=request.POST.get('electionname')
        enddate=request.POST.get('enddate')
        AvailableElection.objects.create(election_name=electionname,end_time=enddate)
        messages.success(request,'election has been created successfully')
        return redirect('add-election')
    return render(request,'add-election.html',contex)
@login_required(login_url='admin-login')
def Add_candidate(request):
    today = date.today()
    elections=AvailableElection.objects.filter(end_time__gt=today).order_by('-id')
    if request.method == 'POST':
        election_name=request.POST.get('election_name')
        name=request.POST.get('name')
        partyname=request.POST.get('partyname')
        address=request.POST.get('address')
        party_img=request.FILES.get('party_img')
        candidate_img=request.FILES.get('candidate_img')
        try:
            a_obj=AvailableElection.objects.get(election_name=election_name)
            Candidate.objects.create(election_name=a_obj,name=name,party_name=partyname,address=address,party_img=party_img,candidate_img=candidate_img)
            messages.success(request,'Canditate has been created successfully')
            return redirect('add-candidate')
        except Exception as e:
            messages.warning(request,'There is no any available election here')
            return redirect('add-candidate')
    contex={
        'elections':elections
    }
    return render(request,'add-candidate.html',contex)
@login_required(login_url='admin-login')
def Available_Candidates(request):
    candidate_objs=Candidate.objects.all().order_by('-id')
    contex={
        'candidate_objs':candidate_objs
    }
    return render(request,'viwe-all-candidates.html',contex)
@login_required(login_url='user-login')
def User_Election(request):
    user_object=UserDetails.objects.get(user__username=request.user)
    today = date.today()
    elections=AvailableElection.objects.filter(end_time__gt=today).order_by('-id')
    
    if request.method == 'POST':
        election=request.POST.get('election')
        return redirect('vote',elec=election)
    contex={'user_object':user_object,
            'elections':elections
            }
    return render(request,'user-election.html',contex)
@login_required(login_url='user-login')
def vote(request,elec):
    user_object=UserDetails.objects.get(user__username=request.user)
    candidate_objs=Candidate.objects.filter(election_name__election_name=elec)
    is_voted=None
    try:
        is_voted=Vote.objects.get(user=request.user,election_name__election_name=elec)
        print(is_voted)
    except Exception as e:
        print(e)
    contex={'user_object':user_object,
            'candidate_objs':candidate_objs,
            'is_voted':is_voted,
            }
    return render(request,'vote.html',contex)
@login_required(login_url='user-login')
def Vote_done(request):
    if request.method == 'POST':
        e_id=request.POST.get('e_id')
        c_id=request.POST.get('c_id')
        elec=AvailableElection.objects.get(id=e_id)
        candi=Candidate.objects.get(id=c_id)
        candi.vote_count=candi.vote_count+1
        candi.save()
        vote_obj, created=Vote.objects.get_or_create(election_name=elec,candidate_name=candi)
        
        if not created:
            vote_obj.user.add(request.user)
            vote_obj.save()
        else :
            vote_obj.user.add(request.user)
            vote_obj.save()
        messages.success(request,'Successfully voted')
        return redirect('user-dashboard',user1=request.user)
@login_required(login_url='admin-login')    
def Search_Result(request):
    elections=AvailableElection.objects.all().order_by('-id')
    if request.method == 'POST':
        election=request.POST.get('election')
       
        return redirect('view-result',election=election)
    contex={
        'elections':elections
    }
    return render(request,'view-result-page1.html',contex)
@login_required(login_url='admin-login')
def View_Result(request,election):
    candidate_objs=Candidate.objects.filter(election_name__election_name=election)
    heighest_vote=Vote.objects.alias(num_vote=Count('user')).order_by('-num_vote')[0]
    contex={
        'candidate_objs':candidate_objs,
        'heighest_vote':heighest_vote
    }
    return render(request,'view-result-page2.html',contex)
@login_required(login_url='user-login')
def Change_password(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        oldpassword=request.POST.get('password')
        newpassword=request.POST.get('re-password')
        try:
                user_obj=User.objects.get(email=email)
            
                match_password=check_password(oldpassword,user_obj.password)
                if not match_password:
                    messages.warning(request,'old password is not matched')
                    return redirect('change-password')
                else:
                    user_obj.set_password(newpassword)
                    user_obj.save()
                    messages.success(request,'password changed sucessfully')
                    return redirect('change-password')
        except Exception as e:
           
            messages.warning(request,'email does not exists')
            return redirect('change-password')
    return render(request,'change-password.html')