from django.contrib import admin
from .models import profileModel , HRRS_INTAKE_SCREEN ,DAST,MAST,SOGS,HRRS_RECORD_RELEASE_AUTHORIZATION ,Initial_Treatment_Plan ,HRRS_PROGRESS_NOTE , HRRS_DISCHARGE_PLANNING,chartReviewTool,demoGraphicModel,Grievance_Procedure,Rights_of_Each_Client_or_Bill_of_Rights,case_note,program_rules,consent,program

class profileAdmin(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(profileModel, profileAdmin)
admin.site.register(HRRS_INTAKE_SCREEN)
admin.site.register(DAST)
admin.site.register(MAST)
admin.site.register(SOGS)
admin.site.register(HRRS_RECORD_RELEASE_AUTHORIZATION)
admin.site.register(Initial_Treatment_Plan)
admin.site.register(HRRS_PROGRESS_NOTE)
admin.site.register(HRRS_DISCHARGE_PLANNING)
admin.site.register(chartReviewTool)
admin.site.register(demoGraphicModel)
admin.site.register(Grievance_Procedure)
admin.site.register(Rights_of_Each_Client_or_Bill_of_Rights)
admin.site.register(case_note)
admin.site.register(program_rules)
admin.site.register(consent)
admin.site.register(program)