from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields, ModelForm
from promo.models import Registers

class SignUpForm(UserCreationForm):
    first_name=forms.CharField(max_length=100,label='ชื่อ',required=True)
    last_name=forms.CharField(max_length=100,label='นามสกุล',required=True)
    email=forms.EmailField(max_length=250,label='อีเมลล์',help_text='propung@gmail.com')
    username=forms.CharField(max_length=255,label='ชื่อผู้ใช้',required=True)
    password1 = forms.CharField(label="รหัสผ่าน",strip=False,widget=forms.PasswordInput)
    password2 = forms.CharField(label="ยืนยันรหัสผ่าน",strip=False,widget=forms.PasswordInput)

    class Meta :
        model=User
        fields=('first_name','last_name','username','email','password1','password2')

class registerForm(ModelForm):
    first_name=forms.CharField(max_length=100,required=True)
    last_name=forms.CharField(max_length=100,required=True)
    username=forms.CharField(max_length=100,required=True)
    email=forms.EmailField(max_length=250,required=True,help_text='propung@gmail.com')
    Phone_namber=forms.CharField(max_length=10,required=True,help_text='เบอร์โทรศัพท์ที่ติดต่อได้')
    Prompt_Pay=forms.CharField(max_length=13,required=True,help_text='หมายเลขพร้อมเพย์ **สำคัญ**')
    ID_card=forms.CharField(max_length=13,required=True,help_text='รหัสบัตรประจำตัวประชาชน')
    address=forms.CharField(widget=forms.Textarea,help_text='ที่อยู่ที่สามารถติดต่อได้')
    ZIP_code=forms.CharField(max_length=5,required=True,help_text='รหัสไปรษณีย์')

    class Meta :
        model=Registers
        fields=('first_name','last_name','username','email','Phone_namber','Prompt_Pay','ID_card','address','ZIP_code')