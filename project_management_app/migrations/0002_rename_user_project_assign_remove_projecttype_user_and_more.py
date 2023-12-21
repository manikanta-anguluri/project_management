# Generated by Django 4.1.5 on 2023-01-31 06:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project_management_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='user',
            new_name='assign',
        ),
        migrations.RemoveField(
            model_name='projecttype',
            name='user',
        ),
        migrations.RemoveField(
            model_name='task',
            name='user',
        ),
        migrations.AlterField(
            model_name='task',
            name='assign',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]