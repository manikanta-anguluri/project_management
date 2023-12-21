from django import forms
from .models import Project,Task,ProjectType
from django.contrib.auth.models import User


# status = (
#     ('1', 'Open'),
#     ('2', 'Completed'),
#     ('3', 'Cancelled'),
# )

# active_status = (
#     ('1', 'Yes'),
#     ('2', 'No'),
# )

# priority_status = (
    
#     ('1', 'Medium'),
#     ('2', 'Low'),
#     ('3', 'High'),
# )

# type=(
#     ('1', 'internal'),
#     ('2', 'external'),
# )


class ProjectRegistrationForm(forms.ModelForm):
    # name = forms.CharField(max_length=80)
    # project_type = forms.ModelChoiceField(queryset=ProjectType.objects.all())
    # # project_type = forms.ModelChoiceField(queryset=ProjectType.objects.values_list('type', flat=True).distinct())
    # status = forms.ChoiceField(choices=status)
    # is_active = forms.ChoiceField(choices=active_status)
    # expected_start_date=forms.DateField()
    # expected_end_date=forms.DateField()
    # priority=forms.ChoiceField(choices=priority_status)
    # description = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Project
        fields = ["name",
                  "project_type",
                  "assign",
                  "status",
                  "is_active",
                  "expected_start_date",
                  "expected_end_date",
                  "priority",
                  "description",
                  ]


    def save(self,commit=True):
        Project = super(ProjectRegistrationForm, self).save(commit=False)
        Project.name = self.cleaned_data['name']
        Project.project_type=self.cleaned_data["project_type"]
        Project.assign=self.cleaned_data["assign"]
        Project.status = self.cleaned_data['status']
        Project.is_active = self.cleaned_data['is_active']
        Project.expected_start_date = self.cleaned_data['expected_start_date']
        Project.expected_end_date = self.cleaned_data['expected_end_date']
        Project.priority = self.cleaned_data['priority']
        Project.description = self.cleaned_data['description']
        Project.save()
        
        if commit:
            Project.save()
        return Project


    def __init__(self,*args, **kwargs):
        super(ProjectRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Project Name'  
        self.fields["project_type"].widget.attrs['class']='form-control'
        self.fields["assign"].widget.attrs['class']='form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['is_active'].widget.attrs['class'] = 'form-control'
        self.fields['expected_start_date'].widget.attrs['class'] = 'form-control'
        self.fields['expected_end_date'].widget.attrs['class'] = 'form-control'
        self.fields['priority'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['placeholder'] = 'project description...'

   

class ProjectTypeForm(forms.ModelForm):
    # type=forms.CharField(max_length=100)
    class Meta:
        model = ProjectType
        fields = ["type"]
    
    def save(self, commit=True):
        projecttype = super(ProjectTypeForm, self).save(commit=False)
        projecttype.type = self.cleaned_data['type']
        projecttype.save()

        if commit:
            projecttype.save()

        return projecttype

    def __init__(self, *args, **kwargs):
        super(ProjectTypeForm, self).__init__(*args, **kwargs)
        self.fields['type'].widget.attrs['class'] = 'form-control'
        self.fields['type'].widget.attrs['placeholder'] = 'project type'

class TaskRegistrationForm(forms.ModelForm):
    # task_name = forms.CharField(max_length=80)
    # project = forms.ModelChoiceField(queryset=Project.objects.all())
    # assign = forms.ModelChoiceField(queryset=NormalUser.objects.all())
    # status = forms.ChoiceField(choices=status)
    # type=forms.ChoiceField(choices=type)
    # expected_start_date=forms.DateField()
    # expected_end_date=forms.DateField()
    # priority=forms.ChoiceField(choices=priority_status)
    # description = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Task
        fields = ["task_name",
                  "project",
                  "assign",
                  "status",
                  "type",
                  "expected_start_date",
                  "expected_end_date",
                  "priority",
                  "description",
                  ]

   
    def save(self, commit=True):
        task = super(TaskRegistrationForm, self).save(commit=False)
        task.task_name = self.cleaned_data['task_name']
        task.project = self.cleaned_data['project']
        task.status = self.cleaned_data['status']
        task.type = self.cleaned_data['type']
        task.expected_start_date = self.cleaned_data['expected_start_date']
        task.expected_end_date = self.cleaned_data['expected_end_date']
        task.priority = self.cleaned_data['priority']
        task.description = self.cleaned_data['description']
        task.save()

        if commit:
            task.save()

        return task


    def __init__(self,*args, **kwargs):
        super(TaskRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['task_name'].widget.attrs['class'] = 'form-control'
        self.fields['task_name'].widget.attrs['placeholder'] = 'task name'
        self.fields['project'].widget.attrs['class'] = 'form-control'
        self.fields['project'].widget.attrs['placeholder'] = 'select project'
        self.fields['assign'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['type'].widget.attrs['class'] = 'form-control'
        self.fields['expected_start_date'].widget.attrs['class'] = 'form-control'
        self.fields['expected_end_date'].widget.attrs['class'] = 'form-control'
        self.fields['priority'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['placeholder'] = 'task description..'

    
        