from django import forms
from .models import Articles, News

class LoginForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={"class": 'login-field', 'placeholder': "Ім\'я"}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={"class": 'login-field', 'placeholder': "Пароль"}))

 
class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['name', 'content', 'icon']
        labels = {
            "name": "",
            "content": "",
            "icon": "",
        }
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'create_field create_field_name',
                'placeholder': 'Назва'
            }),
            'content': forms.Textarea(attrs={
                'class': 'create_field create_field_area',
                'placeholder': 'Зміст'
            })
        }
        
class CreateNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['name', 'content', 'icon']
        labels = {
            "name": "",
            "content": "",
            "icon": "",
        }
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'create_field create_field_name',
                'placeholder': 'Назва'
            }),
            'content': forms.Textarea(attrs={
                'class': 'create_field create_field_area',
                'placeholder': 'Зміст'
            })
        }