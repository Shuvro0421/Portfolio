# Generated by Django 3.2.9 on 2021-12-15 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myportfolio', '0005_rename_fll_exam_name_education_full_exam_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='profile_image',
            field=models.ImageField(blank=True, default='images/profile_picture/Default.jpg', null=True, upload_to='images/profile_picture/'),
        ),
    ]
