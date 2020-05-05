from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'px-3 w-full py-2 bg-gray-200 border border-gray-200 rounded focus:border-gray-400 focus:outline-none focus:bg-white mb-4',
                                                             'name' : 'email', 'id' : 'email', 'placeholder' : 'Student ID' }), required='autofocus')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'px-3 w-full py-2 bg-gray-200 border border-gray-200 rounded focus:border-gray-400 focus:outline-none focus:bg-white mb-4',
                                                             'name' : 'password', 'type' : 'password', 'id' : 'password', 'placeholder' : 'Password' }))