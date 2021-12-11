from django import forms  
from .models import * 

class UsersModelForm(forms.ModelForm):
    class Meta:
        model = UsersModel
        fields = "__all__"


class ProductModelForm(forms.ModelForm):  
    class Meta:  
        model = ProductsModel  
        fields = "__all__"  

class CallLogsModelForm(forms.ModelForm):
    class Meta:
        model = CallLogsModel
        fields = "__all__"