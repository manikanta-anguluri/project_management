from django.shortcuts import  render, redirect
from .forms import RegistrationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from .forms import CompanyRegistrationForm
from .models import Company,UserProfile
from .forms import ProfilePictureForm
from django.contrib.auth.models import User

def register_request(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful.")
			return redirect("register_app:new-company")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = RegistrationForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

  

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("base_app:index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("base_app:home")


def userDelete(request, id):
  user_object = User.objects.get(id=id)
  user_object.delete()
  return redirect("register_app:users")

def userUpdateView(request, id):
    objects = User.objects.get(id=id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=objects)
        if form.is_valid():
            form.save()
            return redirect("register_app:users")
    else:
        form = RegistrationForm(instance=objects)
    return render(request,"user_update.html",{'form': form,"objects":objects})   

def usersView(request):
    if request.user.is_superuser:
        users = User.objects.all()
    else:
        users=User.objects.filter(user=request.user)    
    context = {
        'users' : users
    }
    return render(request, 'users_view.html', context)        
	    


def newCompany(request):
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST)
        context = {'form':form}
        if form.is_valid():
            obj= form.save(commit=False)
            obj.user= request.user
            obj.save()
            created = True
            form = CompanyRegistrationForm()
            context = {
                'created' : created,
                'form' : form,
                       }
            return redirect("base_app:index")
        else:
            return render(request, 'new_company.html', context)
    else:
        form = CompanyRegistrationForm()
        context = {
            'form' : form,
        }
        return render(request, 'new_company.html', context)

def companyUpdateView(request, id):
    objects = Company.objects.get(id=id)
    if request.method == 'POST':
        form = CompanyRegistrationForm(request.POST, instance=objects)
        if form.is_valid():
            form.save()
            return redirect("register_app:company")
    else:
        form = CompanyRegistrationForm(instance=objects)
    return render(request,"company_update.html",{'form': form,"objects":objects})      
	
def companyDelete(request, id):
  project_object = Company.objects.get(id=id)
  project_object.delete()
  return redirect("register_app:company")

def companyView(request):
    if request.user.is_superuser:
        companies = Company.objects.all()
    else:
        companies=Company.objects.filter(user=request.user)   
    context = {
        'companies' : companies,
    }
    return render(request, 'company_view.html', context)   
      	
def profile(request):
	# profile_user = request.user.userprofile
	form = ProfilePictureForm()
	if request.method == 'POST':
		form = ProfilePictureForm(request.POST, request.FILES,instance=request.user.userprofile)
		if form.is_valid():
			form.save()
	context = {'form':form}
	return render(request, 'profile.html', context)





   
