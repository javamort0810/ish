# Generated by Django 4.1.1 on 2022-10-05 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_rename_ragam_talaba_yosh'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='talaba',
            name='soni_kt',
        ),
    ]
