# Generated by Django 4.1.1 on 2022-10-07 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_records'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='kitob',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.kitob'),
        ),
    ]