from django import forms

class Login(forms.Form):
    username=forms.CharField(label="Kullanıcı Adı")
    password= forms.CharField(label="Şifre",widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username=forms.CharField(max_length=50,label="Kullanıcı Adı")
    email=forms.EmailField(max_length=30,label="E-posta")
    password=forms.CharField(max_length=20,label="Şifre",widget=forms.PasswordInput)
    confirm=forms.CharField(max_length=20,label="Şifre Doğrula",widget=forms.PasswordInput)
    agree_terms1 = forms.BooleanField(required=True,label='Üyelik şartları ve koşullar')
    agree_terms2=forms.BooleanField(required=True,label="Uzaktan satış sözleşmesi")

    def clean(self):
        username=self.cleaned_data.get("username")
        password=self.cleaned_data.get('password')
        confirm=self.cleaned_data.get('confirm')
        agree_terms1=self.cleaned_data.get('agree_terms')
        agree_terms2=self.cleaned_data.get('agree_terms2')
        email=self.cleaned_data.get('email')
        if password and confirm and password !=confirm:
            raise forms.ValidationError('Şifreler Eşleşmiyor.')
        elif agree_terms1 and agree_terms2 is False:
            raise forms.ValidationError('Checkbox İşaretlenmedi')
        values={
            "username":username,
            "password":password,
            "agree_terms":agree_terms1,
            "agree_terms2":agree_terms2,
            "email":email
            
        }
        return values

