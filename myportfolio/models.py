from django.db import models
from datetime import datetime, date

#personal information
class personal_info(models.Model):
    first_name = models.CharField(max_length=32,null=False,blank=False)
    middle_name = models.CharField(max_length=16, null=True, blank=True)
    last_name = models.CharField(max_length=32, null=True, blank=True)
    fathers_name = models.CharField(max_length=48, null=True, blank=True)
    mothers_name = models.CharField(max_length=48, null=True, blank=True)
    date_of_birth = models.DateField(auto_now_add=False, auto_now=False, null=True, blank=True)
    present_address = models.TextField(max_length=256, null=True, blank=True)
    permanent_address = models.TextField(max_length=256, null=True, blank=True)
    religion = models.CharField(max_length=16, null=True, blank=True)
    marital_status = models.CharField(max_length=16, null=True, blank=True)
    blood_group = models.CharField(max_length=4, null=True, blank=True)
    nationality = models.CharField(max_length=24, null=True, blank=True)
    e_mail = models.EmailField(max_length=64, null=True, blank=True)
    phone_number = models.CharField(max_length=24, null=True, blank=True)
    nid = models.CharField(max_length=32, null=True, blank=True)
    birth_certificate_no = models.CharField(max_length=32, null=True, blank=True)
    passport_no = models.CharField(max_length=32, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='images/profile_picture/', default='images/profile_picture/Default.jpg')
    
    class Meta:
        verbose_name_plural = "Personal Info"

    def __str__(self):
        return self.first_name
#education
class education(models.Model):
    personal_info= models.ForeignKey('personal_info',on_delete=models.CASCADE,default=None)
    short_exam_name = models.CharField(max_length=8 , null=False, blank=False)
    full_exam_name = models.CharField(max_length=32 , null=False, blank=False)
    institution_name = models.CharField(max_length=128 , null=False, blank=False)
    group = models.CharField(max_length=16 , null=False, blank=False)
    subject = models.CharField(max_length=64, null=False, blank=False)
    passing_year = models.IntegerField(null=False, blank=False)
    board = models.CharField(max_length=4, null=False, blank=False)
    result = models.CharField(max_length=4, null=False, blank=False)
    class Meta:
        verbose_name_plural = "Education"
        def __str__(self):
                return self.first_name + ' ' + self.middle_name + ' ' + self.last_name
#service
class service(models.Model):
    personal_info= models.ForeignKey('personal_info',on_delete=models.CASCADE,default=None)
    service_title=models.CharField(max_length=50, null=True, blank=True)
    service_description=models.CharField(max_length=50, null=True, blank=True)
    class Meta:
        verbose_name_plural = "Service"
        def __str__(self):
                return self.first_name + ' ' + self.middle_name + ' ' + self.last_name
#skills
class skills(models.Model):
    personal_info= models.ForeignKey('personal_info',on_delete=models.CASCADE,default=None)
    skill_name=models.CharField(max_length=50, null=True, blank=True)
    skill_description=models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Skills"
        def __str__(self):
                return self.first_name + ' ' + self.middle_name + ' ' + self.last_name
#team
class team(models.Model):
    personal_info= models.ForeignKey('personal_info',on_delete=models.CASCADE,default=None)
    team_member_name=models.CharField(max_length=30, null=True, blank=True)
    team_member_occupation=models.CharField(max_length=20, null=True, blank=True)
    team_member_experties=models.CharField(max_length=200, null=True, blank=True)
    team_member_contact=models.CharField(max_length=20, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='images/profile_picture/', default='images/profile_picture/Default.jpg')
    class Meta:
        verbose_name_plural = "Team"
        def __str__(self):
                return self.first_name + ' ' + self.middle_name + ' ' + self.last_name
#hobby
class hobby(models.Model):
    personal_info= models.ForeignKey('personal_info',on_delete=models.CASCADE,default=None)
    hobby_list = models.CharField(max_length=100, null=True, blank=True)
    hobby_description = models.CharField(max_length=500, null=True, blank=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='images/profile_picture/', default='images/profile_picture/Default.jpg')
    class Meta:
        verbose_name_plural = "Hobby"
        def __str__(self):
                return self.first_name + ' ' + self.middle_name + ' ' + self.last_name




