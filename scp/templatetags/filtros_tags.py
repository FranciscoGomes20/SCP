from django import template

register = template.Library()

@register.filter(name='addclassUsername')
def addclassUsername(value):
    return value.as_widget(attrs={
        'type' : 'email',
        'class' : 'form-control',
        'placeholder': 'Username'
    })

@register.filter(name='addclassPassword')
def addclassPassword(value):
    return value.as_widget(attrs={
        'type' : 'password', 
        'class' : 'form-control',
        'placeholder' : 'Password'
    })