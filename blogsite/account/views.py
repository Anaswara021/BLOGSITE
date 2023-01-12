from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView,TemplateView
from .forms import SignupForm,SigninForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.urls import reverse_lazy
# Create your views here.

# class Homee(View):
#     def get(self,req):
#             return render(req,"homes.html")

class Homee(TemplateView):
    template_name="homes.html"

# class Signup(View):
#     def get(self,request):
#         form=SignupForm()
#         return render(request,"register.html",{'form':form})
#     def post(self,request):
#         form_data=SignupForm(request.POST)
#         if form_data.is_valid():
#             form_data.save()
#             messages.success(request,"Registration completed")
#             return redirect('home')
#         else:
#             messages.error(request,"Registration failed")
#             return redirect('regi')



class Signup(CreateView):
    model=User
    form_class=SignupForm
    template_name='register.html'
    success_url=reverse_lazy('home')
    
    # def post(self,request,*args,**kwargs):
    #     form_data=self.form_class(request.POST)
    #     if form_data.is_valid():
    #         email_id=form_data.cleaned_data.get('email')
    #         form_data.save()
    #         send_mail(
    #             'BlogApp Registration',
    #             'You are succesfully registred in BlogApp',
    #             'anaswara021@gmail.com',
    #             [email_id],
    #             fail_silently=True
    #         )
    #         messages.success(request,"Registration Completed!!!")
    #         return redirect('home')
    #     else:
    #         messages.error(request,"Registration Failed!!!")
    #         return render(request,"register.html",{'form':form_data})



    
    def post(self,request,*args,**kwargs):
        form_data=self.form_class(request.POST)
        if form_data.is_valid():
            email_id=form_data.cleaned_data.get('email')
            uname=form_data.cleaned_data.get('username')
            pwd=form_data.cleaned_data.get('password1')
            msg="You are registered in Blogapp.\n Your username:"+str(uname)+"\n password:"+str(pwd)
            form_data.save()
            send_mail(
                'BlogApp Registration',
                msg,
                'anaswara021@gmail.com',
                [email_id],
                fail_silently=True
            )
            messages.success(request,"Registration Completed!!!")
            return redirect('home')
        else:
            messages.error(request,"Registration Failed!!!")
            return render(request,"register.html",{'form':form_data})


# class Signin(View):
#     def get(self,request):
#          form=SigninForm()
#         #  print(request.User)
#          return render(request,"log.html",{'form':form})
#     def post(self,request):
#         uname=request.POST.get('username')
#         psw=request.POST.get('password')
#         user=authenticate(request,username=uname,password=psw)
#         if user:
#             # return HttpResponse("user login success")
#             login(request,user)
#             return redirect('uhome')
#         else:
#             # return HttpResponse("User login failed")
#              return redirect('logi')

class Signin(FormView):
    form_class=SigninForm
    template_name='log.html'
    def post(self,request):
        uname=request.POST.get('username')
        psw=request.POST.get('password')
        user=authenticate(request,username=uname,password=psw)
        if user:
    
            login(request,user)
            return redirect('upro')
        else:
            return redirect('logi')
         

class SignOut(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("logi")
       



