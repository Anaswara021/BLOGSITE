from  django import forms
from account.models import Userprofile
from .models import BlogModel,Comments

class UserProForm(forms.ModelForm):
    class Meta:
        model=Userprofile
        exclude=['users']

class PassForm(forms.Form):
    old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    confirm_password=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))


class BlogForm(forms.ModelForm):
     class Meta:
        model=BlogModel
        fields=['title','content','image']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.Textarea(attrs={'class':'form-control'}),
            'image':forms.FileInput(attrs={'class':'form-control'})
        }
class CommentForm(forms.ModelForm):
    class Meta:
       model=Comments
       fields=['Comment']
       widgets={
           'Comment':forms.Textarea(attrs={'class':'form-control'})
       }