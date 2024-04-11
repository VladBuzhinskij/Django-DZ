from django import forms

CHOICES= [
    ('year', 'Год'),
    ('month', 'Месяц'),
    ('week', 'Неделя'),
    ]
class UserForm(forms.Form):
    # sort= forms.CharField(label='sort', widget=forms.RadioSelect(choices=CHOICES))
    ...