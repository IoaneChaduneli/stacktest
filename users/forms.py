from django import forms
from users.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from users.models import Profile

class UserCreationForm(forms.ModelForm):
    confirm_password = forms.CharField(validators=[
                                    validate_password],
                                    widget=forms.PasswordInput())
    class Meta:
        model = User  
        fields = [
            'username',
            'password',
            'confirm_password'
        ]
        widgets = {
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput()
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('confirm_password')

        if password != password2:
            raise ValidationError({
                'password': "Passwords does not match!",
                'confirm_password': 'Passwords does not match!',
            })
        return cleaned_data
    
    def save(self, commit: bool = False) :
        user: User = super().save(False)
        user.set_password(user.password)
        user.save(commit)
        return user

class Profileform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('icon',)
    