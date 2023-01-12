# Create your views here.
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import View,CreateView,TemplateView,FormView,UpdateView
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from account.models import Userprofile
from .models import BlogModel,Comments
from django.contrib import messages
from .forms import UserProForm,PassForm,BlogForm,CommentForm
from django.contrib.auth import authenticate 
# from .forms import SignupForm,SigninForm
# from django.contrib import messages
# from django.contrib.auth import authenticate
# from django.http import HttpResponse
# Create your views here.

# decorators
def signin_required(fn):  
    def wrapper(req,*args,**kwargs):
        if req.user.is_authenticated:
            return fn(req,*args,**kwargs)
        else:
            return redirect('logi')
    return wrapper


# @method_decorator(signin_required,name='dispatch')
# class User(View):
#     def get(self,req,*args,**kwargs):
#         user=req.user
#         return render(req,"uhome.html",{"user_data":user})
# # class Homee(TemplateView):
# #     template_name="homes.html"


@method_decorator(signin_required,name='dispatch')
class User(CreateView):
    template_name="uhome.html"
    form_class=BlogForm
    model=BlogModel
    success_url=reverse_lazy("uhome")
    def form_valid(self, form):
        form.instance.author=self.request.user
        self.object = form.save()
        messages.success(self.request, 'Bio added succesfuly')
        return super().form_valid(form)
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        blog=self.model.objects.all().order_by('-Date')
        context['blog']=blog
        cmnt=CommentForm()
        context['Comment']=cmnt
        context['cmnts']=Comments.objects.all()
        return context


        
def AddComment(request,*args,**kwargs):
    if request.method=='POST':
        cmnt=request.POST.get('Comment')
        user=request.user
        blog_id=kwargs.get('id')
        blog=BlogModel.objects.get(id=blog_id)
        Comments.objects.create(Comment=cmnt,user=user,blog=blog)
        messages.success(request,"Comment Added")
        return redirect('uhome')


def add_like(request,*args,**kwargs):
    blog_id=kwargs.get('bid')
    user=request.user
    blog=BlogModel.objects.get(id=blog_id)
    blog.liked_by.add(user)
    blog.save()
    return redirect('uhome')
    


# @method_decorator(signin_required,name='dispatch')
# class ViewProfile(View):
#     def get(self,req,*args,**kwargs):
#         # if req.user.is_authenticated:
#            user=req.user
#            return render(req,"profile.html",{"user_data":user})


# @method_decorator(signin_required,name='dispatch')
# class ViewProfile(View):
#     def get(self,req,*args,**kwargs):
#         # if req.user.is_authenticated:
#            user=req.user
#            return render(req,"profile.html",{"user_data":user})


@method_decorator(signin_required,name='dispatch')
class Viewprofile(TemplateView):
    template_name="profile.html"



class UserProView(CreateView):
    model=Userprofile
    form_class=UserProForm
    template_name="bio.html"
    success_url=reverse_lazy('upro')
    # def post(self,req,*args,**kwargs):
    #     form_data=self.form_class(req.POST,req.FILES)
    #     if form_data.is_valid():
    #        form_data.instance.user=req.user
    #        form_data.save()
    #        return redirect('upro')
    #     else:
    #        return redirect('addbio')


        #    DELETED
        # else:
        #      return redirect('logi')
    def form_valid(self, form):
        form.instance.user=self.request.user
        self.object = form.save()
        messages.success(self.request, 'Bio added succesfuly')
        return super().form_valid (form)

class Changepassword(FormView):
    template_name='pchange.html'
    form_class=PassForm

    def post(self,request,*args,**kwargs):
      form_data=self.form_class(request.POST)
      if form_data.is_valid():
        old=form_data.cleaned_data.get('old_password')
        new_p=form_data.cleaned_data.get('new_password')
        c_p=form_data.cleaned_data.get('confirm_password')
        user=authenticate(request,username=request.user.username,password=old)
        if user:
            if new_p==c_p:
                user.set_password(c_p)
                user.save()
                messages.success(request,"password changed!!")
                return redirect('logi')
            else:
                messages.error(request,"new password and confirm password mismatches!!")
                return redirect('change-password')
        else:
            messages.error(request,"old password missmatches!!")
            return redirect('change-password')
      else:
         messages.error(request,form_data.errors)
         return redirect('change-password')


class UpdateBioview(UpdateView):
    template_name='upbio.html'
    form_class=UserProForm
    model=Userprofile
    success_url=reverse_lazy('upro')
    pk_url_kwarg='user_id'
    def form_valid(self, form):
       self.object = form.save()
       messages.success(self.request,'Bio updated!')
       return super().form_valid (form)
    
class MyBlogs(TemplateView):
    template_name='blogs.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        blog=BlogModel.objects.filter(author=self.request.user)
        context['data']=blog
        context['cmnts']=Comments.objects.all()
        return context    


