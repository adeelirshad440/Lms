from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.regex_helper import Choice
from app_users.models import UserProfileInfo


class UserForm(UserCreationForm):
    email = forms.EmailField()

    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

        labels = {
            'password1': 'Password',
            'password2': 'Confirm Password'
        }


class UserProfileInfoForm(forms.ModelForm):
    bio = forms.CharField(max_length=150)
    teacher = 'teacher'
    student = 'student'
    parent = 'parent'

    user_types = [
        (teacher, 'teacher'),
        (student, 'student'),
        (parent, 'parent')
    ]
    user_type = forms.ChoiceField(choices=user_types, required=True)

    class Meta():
        model = UserProfileInfo
        fields = ('bio', 'profile_pic', 'user_type')
