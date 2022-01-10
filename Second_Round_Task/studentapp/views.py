from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import Studentinfo,StudentAcademics
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from .forms import StudentInfoForm,StudentAcademicsForm 
from django.contrib import messages

def index(request):
    stuinfo = Studentinfo.objects.all()
    return render (request,'studentapp/index.html',context={'students':stuinfo})

## This view is called when user logged out
def base_index(request):
    stuinfo = Studentinfo.objects.all()
    return render (request,'studentapp/base_index.html',context={'students':stuinfo})

def signup(request):
    form = UserCreationForm() 
    if request.POST:
        form =  UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('login')
    
    return render (request,'studentapp/signup.html',{"form":form})

@login_required
def create_student_details(request):
    stu_info_form = StudentInfoForm()
    stu_acad_form = StudentAcademicsForm()
    if request.POST:
        
        stu_info_form = StudentInfoForm(request.POST)
        stu_acad_form = StudentAcademicsForm(request.POST)

        if stu_info_form.is_valid() and stu_acad_form.is_valid():
            stu_info_object = stu_info_form.save()
            stu_acad_form.instance.roll_no_id = stu_info_object
            stu_acad_form.save()
            return redirect ('index')
        

    return render (request,'studentapp/create_stu_detail.html',{'form1':stu_info_form,'form2':stu_acad_form})

@login_required
def display_student_details(request,id):
    info_object = Studentinfo.objects.get(pk = id)
    acad_object = info_object.studentacademics_set.all()[0]

    return render (request,'studentapp/display_student_details.html',context={'info':info_object,'acad':acad_object})

@login_required
def update_student_details(request,id):
    info_object = Studentinfo.objects.get(pk = id)
    acad_object = info_object.studentacademics_set.all()[0]
    stu_info_form = StudentInfoForm(instance=info_object)
    stu_acad_form = StudentAcademicsForm(instance=acad_object)
    if request.POST:
        stu_info_form = StudentInfoForm(request.POST,instance=info_object)
        stu_acad_form = StudentAcademicsForm(request.POST,instance=acad_object)

        if stu_info_form.is_valid() and stu_acad_form.is_valid():
            stu_info_object = stu_info_form.save()
            stu_acad_form.instance.roll_no_id = stu_info_object
            stu_acad_form.save()

            return redirect (reverse('display',args=[stu_info_object.roll_no]))

    return render (request,'studentapp/update_student_details.html',context={'form1':stu_info_form,'form2':stu_acad_form})
    
@login_required
def delete_student_details(request,id):
    info_object = Studentinfo.objects.get(pk = id)
    if request.POST:
        info_object.delete()
        return redirect ('index')
    return render (request,'studentapp/delete_student_details.html',context={'info':info_object})

def search_name(request):
    if len(request.GET['search']) == 0:
       return redirect ('index') 
    else :
        data = request.GET['search']
        stu_info_obj = Studentinfo.objects.filter(name__icontains = data)
        if len(stu_info_obj) == 0:
            messages.info(request, "No Items Matches Your Search")
            return render (request,'studentapp/index.html')
        else :   
            context = {
                    'students': stu_info_obj,
                }
            return render (request,'studentapp/index.html',context)

def change_password(request):
    form = PasswordChangeForm(user=request.user)
    if request.POST:
        form = PasswordChangeForm(user=request.user,data = request.POST)
        if form.is_valid():
            update_session_auth_hash(request, form.user)
            form.save()
            return redirect ('login')
    
    return render (request,'studentapp/password_change.html',{'form':form})


