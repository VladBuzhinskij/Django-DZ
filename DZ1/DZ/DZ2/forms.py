from django import forms
from DZ2.models import Userss
CHOICES= [
    ('year', 'Год'),
    ('month', 'Месяц'),
    ('week', 'Неделя'),
    ]
class UserForm(forms.Form):
    # sort= forms.CharField(label='sort', widget=forms.RadioSelect(choices=CHOICES))
    ...

class ProfileForm(forms.ModelForm):
    name=forms.CharField( max_length=150)
    email=forms.EmailField(max_length=150)
    phone_number=forms.CharField( max_length=150)
    address=forms.CharField()
    image=forms.ImageField(required=False)
    class Meta:
        model=Userss
        fields=(
            "name",
            "email",
            "phone_number",
            "address",
            "image",
            
        )