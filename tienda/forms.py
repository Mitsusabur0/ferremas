from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import Profile




# Registrar usuario
class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Correo electrónico'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'Usuario'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Letras, números y @/./+/-/_.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Debe contener al menos 8 caracteres.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar contraseña'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Ingrese la contraseña nuevamente.</small></span>'



# Editar usuario
class UpdateUserForm(UserChangeForm):
    password = None
    email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Correo electrónico'}), required=False)
    first_name = forms.CharField(label="Nombre", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}), required=False)
    last_name = forms.CharField(label="Apellido", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'Usuario'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].label = 'Usuario'
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Letras, números y @/./+/-/_.</small></span>'


class ChangePasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ["new_password1", "new_password2"]
    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['new_password1'].label = ''
        self.fields['new_password1'].help_text = '<ul class="form-text text-muted small"><li>Debe contener al menos 8 caracteres.</li></ul>'

        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirmar contraseña'
        self.fields['new_password2'].label = ''
        self.fields['new_password2'].help_text = '<span class="form-text text-muted"><small>Ingrese la contraseña nuevamente.</small></span>'




class UserInfoForm(forms.ModelForm):
    phone = forms.CharField(label="Teléfono", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Teléfono"}), required=False)
    address1 = forms.CharField(label="Dirección", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Dirección"}), required=False)
    # address2 = forms.CharField(label="Dirección 2", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Dirección 2"}), required=False)
    city = forms.CharField(label="Ciudad", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Ciudad"}), required=False)

    class Meta:
        model = Profile
        fields = ("phone", "address1", "city")