from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [
    url(r'^$',views.home, name = "home"),
    url(r'login/', views.login_user, name = 'login'),
    url(r'^logout/$', views.logout_user, name= "logout"),

    #----------------------------------------------------------------------------
    url(r'^profile/(?P<user_name>\w+)/$', views.profile_user, name= "profile"),
    #---------------------------------------------------------------------------
    url(r'^register/$', views.register_user, name= "register"),
    url(r'^edit_profile/$', views.edit_profile, name = "edit_profile"),
    url(r'^dashbaord/$', views.dashboard, name = "dashboard"),
    
    #Password Change URL............
    url(r'^change_password/$', views.change_password, name = "change_password"),

    #password Reset URLS...........
    path('password_reset/', PasswordResetView.as_view(), name='password_reset' ),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    #Email Confirm URLs.....
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),

    #Contact Us Page ...
    url(r'^contact/$', views.contact, name="contact"),

    #####   APP URLS #################

    url(r'^HRRS_INTAKE_SCREEN/$', views.HRRS_INTAKE_SCREEN_view, name="HRRS_INTAKE_SCREEN"),
    url(r'^DAST/$', views.DAST_view, name="DAST"),
    url(r'^MAST/$', views.MAST_view, name="MAST"),
    url(r'^SOGS/$', views.SOGS_view, name="SOGS"),
    url(r'^HRRS_RECORD_RELEASE_AUTHORIZATION/$', views.HRRS_RECORD_RELEASE_AUTHORIZATION_view, name="HRRS_RECORD_RELEASE_AUTHORIZATION"),
    url(r'^HRRS_PROGRESS_NOTE/$', views.HRRS_PROGRESS_NOTE_view, name="HRRS_PROGRESS_NOTE"),
    url(r'^Initial_Treatment_Plan/$', views.Initial_Treatment_Plan_view, name="Initial_Treatment_Plan"),
    url(r'^HRRS_DISCHARGE_PLANNING/$', views.HRRS_DISCHARGE_PLANNING_view, name="HRRS_DISCHARGE_PLANNING"),
    #url(r'^gen/(?P<user>[-\w]+)/$',views.GeneratePdf1,name="gen"),
    url(r'^GeneratePdf/(?P<user>[-\w]+)/$',views.GeneratePdf,name='GeneratePdf'),
    url(r'^home1/$', views.home1, name="home1"),
    url(r'^demoForm/$', views.demoForm, name="form_2"),
    url(r'^Grievance_Procedure/$', views.Grievance_Procedure_view, name="Grievance_Procedure"),
    url(r'^Rights_of_Each_Client_or_Bill_of_Rights/$', views.Rights_of_Each_Client_or_Bill_of_Rights_view, name="Rights_of_Each_Client_or_Bill_of_Rights"),
    url(r'^case_note/$', views.case_note_view, name="case_note"),
    url(r'^consent/$', views.consent_view, name="consent"),
    url(r'^program_rules/$', views.program_rules_view, name="program_rules"),
    url(r'^program/$', views.program_view, name="program"),
    url(r'^fill/$', views.fill_survey, name="fill"),
    url(r'^conf/$', views.conf, name="conf"),
    url(r'^genpdf/$', views.genpdf, name="genpdf"),


]