from django import forms  
from .models import MemberForm  #models.py
    
class MemberForm(forms.ModelForm):  
    class Meta:  
        model = MemberForm  
        fields = "__all__"