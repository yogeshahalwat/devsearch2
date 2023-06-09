from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,skill,Message
from django.core.validators import RegexValidator
from django import forms


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="username",
        max_length=30,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z]+$',
                message='Username may only contain alphabets',
                code='invalid_username'
            )
        ]
    )
    first_name = forms.CharField(
        label="Name",
        max_length=30,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\s]+$',
                message='First name may only contain alphabets and spaces.',
                code='invalid_first_name'
            )
        ]
    )

    class Meta:
        model = User
        fields = ["first_name","email","username","password1","password2"]
        labels={
            "first_name":"Name",
        }


    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class profileForm(ModelForm):
    class Meta:
        model=Profile
        fields=["name","email","username","location","short_intro","bio","profile_image","social_linkedin",
                 "social_website","social_youtube","social_twitter",]

    def __init__(self, *args, **kwargs):
        super(profileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

class SkillForm(ModelForm):
    class Meta:
        model=skill
        fields="__all__"
        exclude=["owner"]

    def __init__(self, *args, **kwargs):
        super(SkillForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields=["name","email","subject","body"]

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

