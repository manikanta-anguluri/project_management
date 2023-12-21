from django.contrib import admin
from project_management_app.models import Project,Task,ProjectType

# Register your models here.

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(ProjectType)
