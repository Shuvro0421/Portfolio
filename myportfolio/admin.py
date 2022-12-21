from django.contrib import admin
from .models import personal_info, education, service, skills, team, hobby


class personal_infoAdmin(admin.ModelAdmin):
    list_display=['first_name','religion','phone_number','date_of_birth','nid']
    search_fields=['first_name','last_name','religion','phone_number','nid']
    list_filter=['religion','blood_group']


class educationAdmin(admin.ModelAdmin):
    list_display=['personal_info','short_exam_name','full_exam_name','institution_name','group','subject','passing_year','board','result']
    search_fields=['personal_info','short_exam_name','full_exam_name','institution_name','group','subject','passing_year','board','result']
    list_filter=['passing_year']


admin.site.register(personal_info, personal_infoAdmin)
admin.site.register(education, educationAdmin)
admin.site.register(service)
admin.site.register(skills)
admin.site.register(team)
admin.site.register(hobby)


