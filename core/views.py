from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from .tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
import pdfkit 
from .forms import *
from .models import *
from django.http import FileResponse
from django.template.loader import render_to_string
from io import BytesIO
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.template.loader import get_template

########    IMPORTANT IMPORTS REQUIRED     ##################

from .models import profileModel , HRRS_INTAKE_SCREEN ,DAST,MAST,SOGS,HRRS_RECORD_RELEASE_AUTHORIZATION ,Initial_Treatment_Plan ,HRRS_PROGRESS_NOTE , HRRS_DISCHARGE_PLANNING
from .forms import loginForm, registerForm, EditProfileForm, profileInformForm, contactForm , HRRS_INTAKE_SCREEN_Form,DAST_Form,MAST_Form,SOGS_Form,HRRS_RECORD_RELEASE_AUTHORIZATION_Form,Initial_Treatment_Plan_Form,HRRS_PROGRESS_NOTE_Form,HRRS_DISCHARGE_PLANNING_Form

################################################################
############# PDF ##############################################
from hubai.utils import render_to_pdf

from django.http import HttpResponse

#################################################################
def handler404(request):
    return render(request, '404.html', status=404)

def home(request):
    return render(request, 'music/home.html', )

@login_required()
def dashboard(request):
    return render(request, 'music/dashboard.html')

def login_user(request):
    if request.method!= 'POST':
        form = loginForm()
    else:
        form = loginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.warning(request, 'Usename or password may have been entered incorrectly.')
                return redirect('login')
    return render(request, 'music/login.html', {'form' : form})

def logout_user(request):
    logout(request)
    return redirect('home')

@login_required()
def profile_user(request, user_name):
    message = ''
    try:
        user = User.objects.get(username = user_name)
        editProfile = False
        #print(request.user.username == user_name)
        if (request.user==user):
            if request.user.is_superuser:
                # contactNumber = None
                editProfile = True
            else:
                # contactNumber  = profileModel.objects.get(user = user).contactNumber
                editProfile = True
        else:
            if request.user.is_superuser:
                # contactNumber  = profileModel.objects.get(user = user).contactNumber
                editProfile = False
            else:
                # contactNumber = None
                editProfile = None
    except:
        user=request.user
        if request.user.is_superuser:
            # contactNumber = None
            editProfile = True
            message = user_name + " Doest Not Exists "
        else:
            # contactNumber  = profileModel.objects.get(user = User.objects.get(username = request.user.username)).contactNumber
            editProfile = True
            message = user_name
    return render(request, 'music/profile.html', { 'editProfile' :editProfile, 'user':user, 'message' : message})
    
def register_user(request):
    if request.method!='POST':
        form = registerForm()
        # form_2 = profileInformForm()
    else:
        form = registerForm(request.POST)
        # form_2 = profileInformForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.set_password(form.cleaned_data['password2'])
            user.email = form.cleaned_data['email'].lower()
            user.save()
            profile = profileModel.objects.create(user = user)
            # profile.contactNumber = form_2.cleaned_data['contactNumber']
            profile.save()
            current_site = get_current_site(request)
            message = render_to_string('music/acc_active_email.html', {
                'user':user, 'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            mail_subject = 'Activate your account.'
            to_email = form.cleaned_data.get('email').lower()
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return render(request, 'music/acc_active_email_confirm.html')
    return render(request, 'music/register.html', {'form' : form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return HttpResponse('Activation link is invalid!')

@login_required()
def edit_profile(request):
    if request.method!='POST':
        form = EditProfileForm(instance = request.user)
    else:
        form = EditProfileForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('profile', args=[request.user.username]))
    return render(request, 'music/edit_profile.html',{'form' : form})

@login_required()
def change_password(request):
    if request.method!='POST':
        form = PasswordChangeForm(user = request.user)
    else:
        form = PasswordChangeForm(data = request.POST, user = request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect(reverse('profile', args=[request.user.username]))
    return render(request, 'music/change_password.html' , {'form': form})

def contact(request):
    if request.method!='POST':
        form = contactForm()
    else:
        form = contactForm(request.POST)
        if form.is_valid():
            mail_subject = 'Contact -- By -- ' + form.cleaned_data.get('userName')
            to_email = settings.EMAIL_HOST_USER
            message = form.cleaned_data.get('body')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return redirect('home')
    
    context= {'form' : form}
    return render(request, 'music/contact.html', context)

@login_required()
def HRRS_INTAKE_SCREEN_view(request):
    form = HRRS_INTAKE_SCREEN_Form()
    if request.method== 'POST':
        form = HRRS_INTAKE_SCREEN_Form(request.POST)
        if form.is_valid():
            new= form.save(commit=False)
            new.user=request.user
            new.save()
            form.save()
    context={
        'form':form,
    }
    return render(request,'app/HRRS_INTAKE_SCREEN.html',context)
@login_required()
def DAST_view(request):
    form = DAST_Form()
    if request.method== 'POST':
        form = DAST_Form(request.POST)
        if form.is_valid():
            new= form.save(commit=False)
            new.user=request.user
            new.save()
            form.save()
    context={
        'form':form,
    }
    return render(request,'app/DAST.html',context)
@login_required()
def MAST_view(request):
    form = MAST_Form()
    if request.method== 'POST':
        form = MAST_Form(request.POST)
        if form.is_valid():
            new= form.save(commit=False)
            new.user=request.user
            new.save()
            form.save()
    context={
        'form':form,
    }
    return render(request,'app/MAST.html',context)
@login_required()
def SOGS_view(request):
    form = SOGS_Form()
    if request.method== 'POST':
        form = SOGS_Form(request.POST)
        if form.is_valid():
            new= form.save(commit=False)
            new.user=request.user
            new.save()
            form.save()
    context={
        'form':form,
    }
    return render(request,'app/SOGS.html',context)
@login_required()
def HRRS_RECORD_RELEASE_AUTHORIZATION_view(request):
    form = HRRS_RECORD_RELEASE_AUTHORIZATION_Form()
    if request.method== 'POST':
        form = HRRS_RECORD_RELEASE_AUTHORIZATION_Form(request.POST)
        if form.is_valid():
            new= form.save(commit=False)
            new.user=request.user
            new.save()
            form.save()
    context={
        'form':form,
    }
    return render(request,'app/HRRS_RECORD_RELEASE_AUTHORIZATION.html',context)
@login_required()
def Initial_Treatment_Plan_view(request):
    form = Initial_Treatment_Plan_Form()
    if request.method== 'POST':
        form = Initial_Treatment_Plan_Form(request.POST)
        if form.is_valid():
            new= form.save(commit=False)
            new.user=request.user
            new.save()
            form.save()
    context={
        'form':form,
    }
    return render(request,'app/Initial_Treatment_Plan.html',context)
@login_required()
def HRRS_PROGRESS_NOTE_view(request):
    form = HRRS_PROGRESS_NOTE_Form()
    if request.method== 'POST':
        form = HRRS_PROGRESS_NOTE_Form(request.POST)
        if form.is_valid():
            new= form.save(commit=False)
            new.user=request.user
            new.save()
            form.save()
    context={
        'form':form,
    }
    return render(request,'app/HRRS_PROGRESS_NOTE.html',context)
@login_required()
def HRRS_DISCHARGE_PLANNING_view(request):
    form = HRRS_DISCHARGE_PLANNING_Form()
    if request.method== 'POST':
        form = HRRS_DISCHARGE_PLANNING_Form(request.POST)
        if form.is_valid():
            new= form.save(commit=False)
            new.user=request.user
            new.save() 
            form.save()
    context={
        'form':form,
    }
    return render(request,'app/HRRS_DISCHARGE_PLANNING.html',context)
from django.contrib.auth.models import User

 


@login_required()
def home1(request):
    if request.method !='POST':
        form = chartReviewToolForm()
    else:
        form = chartReviewToolForm(request.POST)
        if form.is_valid():
            new= form.save(commit=False)
            new.user=request.user
            new.save()
            new_chart = form.save()
            context={
                'new_chart' : new_chart
            }
            return redirect('genpdf')
        else:
            return redirect('home')
    context={
        'form' : form,
    }
    return render(request, 'app/homeForm.html', context)

def genpdf(request):

    return render(request, 'app/genpdf.html',{})

@login_required()
def demoForm(request):
    if request.method=="GET":
        context ={
            'form' : demoGraphicForm()
        }
        return render(request, 'app/form_2.html', context)
    elif request.method == "POST" :
        form = demoGraphicForm(request.POST)
        if form.is_valid():
            new= form.save(commit=False)
            new.user=request.user
            new.save()
            obj = form.save()
            context={
                'obj' : obj,
            }
            #return render(request, 'app/demoGraphic.html', context)
        else:
            context ={
            'form' : demoGraphicForm(request.POST)
            }
    return render(request, 'app/form_2.html', context)

    
@login_required()
def generate_pdf(request, form_number):
    obj = demoGraphicModel.objects.get(id= form_number)
    cont={
        'obj' : obj
    }
    message = render_to_string(template_name='forms_app/demoGraphic.html',context=cont)
    config = pdfkit.configuration(wkhtmltopdf="https://drive.google.com/drive/folders/1EMuTSX5fNxVtA4861YcWSQSYtxX9y3jm")
    options = {
        'page-size': 'A4',
        'encoding': "UTF-8",
    'custom-header' : [
        ('Accept-Encoding', 'gzip')
    ],
    'cookie': [
        ('cookie-name1', 'cookie-value1'),
        ('cookie-name2', 'cookie-value2'),
    ],
    'no-outline': None
}
    pdfkit.from_string(message, 'out2.pdf', configuration=config)
    return FileResponse(open('out2.pdf', 'rb'), content_type='application/pdf')



def GeneratePdf(request,user):
    user=User.objects.get(id=user)
    obj=HRRS_INTAKE_SCREEN.objects.get(user=user)
    obj1=DAST.objects.get(user=user)
    obj2=MAST.objects.get(user=user)
    obj3=SOGS.objects.get(user=user)
    obj4=HRRS_RECORD_RELEASE_AUTHORIZATION.objects.get(user=user)
    obj5=HRRS_DISCHARGE_PLANNING.objects.get(user=user)
    obj6=Initial_Treatment_Plan.objects.get(user=user)
    obj7=HRRS_PROGRESS_NOTE.objects.get(user=user)
    obj8=demoGraphicModel.objects.get(user=user)
    obj9=chartReviewTool.objects.get(user=user)
    obj10=Grievance_Procedure.objects.get(user=user)
    obj11=Rights_of_Each_Client_or_Bill_of_Rights.objects.get(user=user)
    obj12=case_note.objects.get(user=user)
    obj13=program_rules.objects.get(user=user)
    obj14=consent.objects.get(user=user)
    obj15=program.objects.get(user=user)

    context = {
    'obj0':obj,
    'i':obj1,
    'j':obj2,
    'k':obj3,
    'l':obj4,
    'm':obj5,
    'n':obj6,
    'o':obj7,
    'obj':obj8,
    'new_chart':obj9,
    'q':obj10,
    'r':obj11,
    'u':obj12,
    't':obj13,
    'x':obj14,
    'y':obj15,
         }
        
    # pdf conversion

    message = render_to_string(template_name='app/pdf.html',context=context)
    #config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
    # options = {
    #     'page-size': 'A4',
    #     'encoding': "UTF-8",
    # 'custom-header' : [
    #     ('Accept-Encoding', 'gzip')
    # ],
    # 'cookie': [
    #     ('cookie-name1', 'cookie-value1'),
    #     ('cookie-name2', 'cookie-value2'),
    # ],
    # 'no-outline': None
    # }
    # pdf = render_to_pdf('app/pdf.html', data)
    # return HttpResponse(pdf, content_type='application/pdf')

    pdfkit.from_string(message, 'out2.pdf')
    return FileResponse(open('out2.pdf', 'rb'), content_type='application/pdf')


def Grievance_Procedure_view(request):
    form = Grievance_Procedure_form()
    if request.method== 'POST':
        form = Grievance_Procedure_form(request.POST)
        if form.is_valid():
            new= form.save(commit=False)
            new.user=request.user
            new.save()
            form.save()
    context={
        'form':form,
    }
    return render(request,'app/Grievance_Procedure.html',context)

def Rights_of_Each_Client_or_Bill_of_Rights_view(request):
    form = Rights_of_Each_Client_or_Bill_of_Rights_form()
    if request.method== 'POST':
        form = Rights_of_Each_Client_or_Bill_of_Rights_form(request.POST)
        if form.is_valid():
            new= form.save(commit=False)
            new.user=request.user
            new.save()
            form.save()
    context={
        'form':form,
    }
    return render(request,'app/Rights_of_Each_Client_or_Bill_of_Rights.html',context)

def case_note_view(request):
    form = case_note_form()
    if request.method== 'POST':
        form = case_note_form(request.POST)
        if form.is_valid():
            new= form.save(commit=False)
            new.user=request.user
            new.save()
            form.save()
    context={
        'form':form,
    }
    return render(request,'app/case_note.html',context)
def program_rules_view(request):
    form = program_rules_form()
    if request.method== 'POST':
        form = program_rules_form(request.POST)
        if form.is_valid():
            new= form.save(commit=False)
            new.user=request.user
            new.save()
            form.save()
    context={
        'form':form,
    }
    return render(request,'app/program_rules.html',context)
def consent_view(request):
    form = consent_form()
    if request.method== 'POST':
        form = consent_form(request.POST)
        if form.is_valid():
            new= form.save(commit=False)
            new.user=request.user
            new.save()
            form.save()
    context={
        'form':form,
    }
    return render(request,'app/consent.html',context)
def program_view(request):
    form = program_form()
    if request.method== 'POST':
        form = program_form(request.POST)
        if form.is_valid():
            new= form.save(commit=False)
            new.user=request.user
            new.save()
            form.save()
    context={
        'form':form,
    }
    return render(request,'app/program.html',context)




def fill_survey(request):
    return render(request,'app/Fill.html',{})
    
def conf(request):
    return render(request,'app/conf.html',{})

