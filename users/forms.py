from django.forms import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','email','username')

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args,**kwargs)

        self.fields["username"].widget.attrs.update({'class': 'form-input'}) 
        self.fields["email"].widget.attrs.update({'class': 'form-input'}) 
        self.fields["first_name"].widget.attrs.update({'class': 'form-input'}) 
        self.fields["last_name"].widget.attrs.update({'class': 'form-input'}) 
        self.fields['password1'].widget.attrs.update({'class': 'form-input'}) 
        self.fields['password2'].widget.attrs.update({'class': 'form-input'}) 

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('first_name','last_name','email','username')