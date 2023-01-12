from django.urls import path
from .views import *

urlpatterns = [
    path('uhome/',User.as_view(),name="uhome"),
    path('upro/',Viewprofile.as_view(),name="upro"),
    path('blogs/',MyBlogs.as_view(),name="blogs"),
    path('addbio/',UserProView.as_view(),name="addbio"),
    path('change-password/',Changepassword.as_view(),name="change-password"),
    path('updatebio/<int:user_id>',UpdateBioview.as_view(),name="updatebio"),
    path('add-cmnt/<int:id>',AddComment,name="add-cmnt"),
    path('add-like/<int:bid>',add_like,name="add-l")
]