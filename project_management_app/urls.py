from django.urls import path
from project_management_app import views

app_name = 'project_management_app'

urlpatterns = [

    path('', views.projectsView, name='projects'),
    path('project/update/<int:id>',views.projectUpdateView,name="project_update"),
    path('project/delete/<int:id>/',views.projectDelete,name='project_delete'),
    path('new-project/', views.newProject, name='new-project'),
    path("project-type/",views.ProjectTypeView,name="project-type"),
    path('new-task/', views.newTask, name='new-task'),
    path('tasks/', views.taskView, name='tasks'),
    path('task/update/<int:id>',views.taskUpdateView,name="task_update"),
    path('task/delete/<int:id>/',views.taskDelete,name='task_delete'),
]
