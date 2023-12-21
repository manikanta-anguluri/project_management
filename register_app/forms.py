from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from register_app.models import Company 
from register_app.models import UserProfile

# Create your forms here.

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        ]

        labels = {
            'first_name': 'Frist Name',
            'last_name': 'Last Name',
        }

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
        return user

    def __init__(self,*args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
      


class CompanyRegistrationForm(forms.ModelForm):
    name = forms.CharField(max_length=80)
    email = forms.EmailField()
    city = forms.CharField(max_length=50)
    found_date = forms.DateField()

    class Meta:
        model = Company
        fields=['name','email','city','found_date']


    def save(self, commit=True):
        company = super(CompanyRegistrationForm, self).save(commit=False)
        company.name = self.cleaned_data['name']
        company.email = self.cleaned_data['email']
        company.city = self.cleaned_data['city']
        company.found_date = self.cleaned_data['found_date']
        company.save()

        if commit:
            company.save()
        return company    


    def __init__(self, *args, **kwargs):
        super(CompanyRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['city'].widget.attrs['class'] = 'form-control'
        self.fields['found_date'].widget.attrs['class'] = 'form-control'
       

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['img']

    def save(self,commit=True):
        pro = super(ProfilePictureForm, self).save(commit=False)
        pro.img = self.cleaned_data['img']

        if commit:
            pro.save()
        return pro

 
   