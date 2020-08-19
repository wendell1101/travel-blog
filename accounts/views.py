from django.shortcuts import render,redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import DetailView
from django.contrib import messages
from accounts.forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from accounts.models import Profile
from articles.models import Category

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'An account has been created for {username}. Login now!')
            return redirect('accounts:login')
    else:
        form = RegisterForm()
    context = {
        'form':form,
    }
    return render(request,'accounts/register.html',context)

class ProfileDetailView(DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'accounts/profile_detail.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetailView,
                        self).get_context_data(*args, **kwargs)
        context['categories'] = Category.objects.all()
        return context

class LoginView(LoginView):
    template_name = 'accounts/login.html'
    context_object_name = 'form'
    
class LogoutView(LogoutView):
    template_name= 'accounts/logout.html'
    
def update_profile(request,slug):
    profile = Profile.objects.get(slug = slug)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance = request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES,instance = profile)
      
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            new_slug = request.POST.get('slug')
            messages.success(request,f'User information has been updated!')
            # return reverse("accounts:profile", kwargs={"slug": slug})
            return HttpResponseRedirect(reverse('accounts:profile', args=[new_slug]))
        else:
            print("user errors:", u_form.errors.as_data())
            print("profile errors:", p_form.errors.as_data())
    else:
        u_form = UserUpdateForm(instance = request.user)
        p_form = ProfileUpdateForm(instance = profile)
    
    context = {
        'p_form': p_form,
        'u_form': u_form,
        'categories': Category.objects.all()
    }
    return render(request,'accounts/profile_update.html',context)