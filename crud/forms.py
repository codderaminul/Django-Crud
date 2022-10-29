from django import forms
from .functions import dateInput,timeInput,datetimeInput
from .models import setFile,setField,singleImage,logIn,roles,signUp
from bootstrap_datepicker_plus.widgets import DateTimePickerInput,DatePickerInput,TimePickerInput

CHOICES_DATA = [('item1', 'item_1'), ('item2', 'item_2')]
Colour_Sample = [
    ('blue', 'Blue'),
    ('black', 'Black'),
    ('green', 'Green'),
]
class fileForm(forms.ModelForm):
    class Meta:
        model = setFile
        fields = "__all__"
        widgets = {
            'jpg_image': forms.FileInput(attrs={'class': 'form-control'}),
            'png_image': forms.FileInput(attrs={'class': 'form-control'}),
            'audio': forms.FileInput(attrs={'class': 'form-control'}),
            'video': forms.FileInput(attrs={'class': 'form-control'}),
            'pdf': forms.FileInput(attrs={'class': 'form-control'}),
            'text': forms.FileInput(attrs={'class': 'form-control'}),
            'doc': forms.FileInput(attrs={'class': 'form-control'}),
            'html': forms.FileInput(attrs={'class': 'form-control'}),
            'css': forms.FileInput(attrs={'class': 'form-control'}),
            'java': forms.FileInput(attrs={'class': 'form-control'}),
            'psd': forms.FileInput(attrs={'class': 'form-control'}),
            'userId':forms.HiddenInput()
        }

class singleImgForm(forms.ModelForm):
    class Meta:
        model = singleImage
        fields = "__all__"
        widgets = {
            'imgname': forms.TextInput(attrs={'class': 'form-control'}),
            'myImg': forms.FileInput(attrs={'class': 'form-control'}),
            #'userId': forms.HiddenInput()
        }

class textForm(forms.ModelForm):
    choice = forms.ChoiceField(choices=CHOICES_DATA, widget = forms.RadioSelect)
    multichoice = forms.MultipleChoiceField(choices=Colour_Sample,widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = setField
        fields = "__all__"
        labels = {'dropdown':'DropDown Menu'}
        help_text = {'characterField':'Enter Character'}
        error_message = {
            'characterField':{'required':'date must be important'},
            'emailField':{'required':'date must be important'},
            'urlField':{'required':'date must be important'},
        }
        widgets = {
            'timeField': timeInput() ,
            'dateField' : dateInput(),
            'datetimeField' : datetimeInput(),
            'dropdown':forms.Select( attrs = {'class':'form-control w-75'}),
            'characterField':forms.TextInput( attrs = {'class':'form-control w-75'}),
            'textField':forms.Textarea( attrs = {'class':'form-control w-75'}),
            'intField':forms.NumberInput( attrs = {'class':'form-control w-75'}),
            'decimalField':forms.NumberInput( attrs = {'class':'form-control w-75'}),
            'durationField':forms.TimeInput( attrs = {'class':'form-control w-75'}),
            'emailField':forms.EmailInput( attrs = {'class':'form-control w-75'}),
            'floatField':forms.NumberInput( attrs = {'class':'form-control w-75'}),
            'jsonField':forms.TextInput( attrs = {'class':'form-control w-75'}),
            'positiveintField':forms.NumberInput( attrs = {'class':'form-control w-75'}),
            'positivebigintField':forms.NumberInput( attrs = {'class':'form-control w-75'}),
            'positivesmallintField':forms.NumberInput( attrs = {'class':'form-control w-75'}),
            'slugField':forms.TextInput( attrs = {'class':'form-control w-75'}),
            'urlField': forms.URLInput(attrs={'class': 'form-control w-75','placeholder':'Enter amy data in Character'}),
            'smallintField':forms.NumberInput( attrs = {'class':'form-control w-75'}),
            'uuidField':forms.TextInput( attrs = {'class':'form-control w-75'}),
            'bigintField':forms.NumberInput( attrs = {'class':'form-control w-75'}),
            'genericipaddrsField': forms.TextInput(attrs={'class': 'form-control w-75'}),
            'image': forms.FileInput(attrs={'class': 'form-control w-75'}),
            'autoslugField': forms.TextInput(attrs={'class': 'form-control w-75'}),
            'binaryField': forms.NumberInput(attrs={'class': 'form-control w-75'}),
            'passwordField': forms.PasswordInput(attrs={'class': 'form-control w-75'}),
            'userId': forms.HiddenInput()
        }

class loginForm(forms.ModelForm):
    class Meta:
        model =logIn
        fields = "__all__"
        widgets = {
            'password':forms.PasswordInput()
        }

class signUpForm(forms.ModelForm):
    repassword = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = signUp
        fields = ['firstName','lastName','userName','email','password','repassword']
        widgets = {
            'password':forms.PasswordInput
        }

