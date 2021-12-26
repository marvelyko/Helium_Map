from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('fullname', 'email','phone')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('fullname', 'email','phone')

        
class RegistrationForm(forms.Form):
    password2 = forms.CharField(max_length=255,required=True)
    password = forms.CharField(max_length=255,required=True)
    email = forms.CharField(max_length=255,required=True)
    fullname = forms.CharField(max_length=255,required=True)
    phone = forms.CharField(max_length=255,required=255)
    
    def clean(self):
        super().clean()
        self.password2 = self.cleaned_data.get("password2")
        self.fullname = self.cleaned_data.get("fullname")
        self.email = self.cleaned_data.get("email")
        self.password = self.cleaned_data.get("password")
        self.phone = self.cleaned_data.get("phone")

        if(self.password2 is None):
            self.errors["password2"] = self.error_class(["არ შეიძლება იყოს ცარიელი"])
        if(self.password is None):
            self.errors["password"] = self.error_class(["არ შეიძლება იყოს ცარიელი"])
        if(self.email is None):
            self.errors["email"] = self.error_class(["არ შეიძლება იყოს ცარიელი"])
        if(self.phone is None):
            self.errors["phone"] = self.error_class(["არ შეიძლება იყოს ცარიელი"])
        if(self.fullname is None):
            self.errors["fullname"] = self.error_class(["არ შეიძლება იყოს ცარიელი"])
        
        if(self.password2 is not None and self.password2 != self.password):
            self.add_error("password2","პაროელბი არ ემთხვევა")

        if(self.password is not None and len(self.password) < 8):
            self.add_error("password","პაროლი უნდა შეიცავდეს მინიმუმ 8 სიმბოლოს")

        if(self.phone is not None):
            if(not self.phone.isdigit()):
                self.add_error("phone","არასწორი ტელეფონის ნომერი")

        return self.cleaned_data


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField()

    # def __init__(self,*args,**kwargs):
    #     super(LoginForm,self).__init__(*args,**kwargs)

    def clean(self):
        self.email = self.cleaned_data.get("email")
        self.password = self.cleaned_data.get("password")
        if(self.email is None):
            self.errors["email"] = self.error_class(["არ შეიძლება იყოს ცარიელი"])
        if(self.password is None):
            self.errors["password"] = self.error_class(["არ შეიძლება იყოს ცარიელი"])

        return self.cleaned_data