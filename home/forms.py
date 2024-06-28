from django.forms import DateTimeField, ModelForm
from django import forms
from .models import Transaction, Renter, Properties
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django.forms.fields import DateField
from django.forms import SelectDateWidget
from django.contrib.admin.widgets import AdminDateWidget
# from django.forms import extras


# Create your forms here.

class NewUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

# class propertyForm(ModelForm):
#     class Meta:
#         model = Properties
#         fields = '__all__'

class DateInput(forms.DateInput):
    input_type = 'date'

class editRenterForm(ModelForm):
    class Meta:
        model = Renter
        fields = ['name','property','homeAddr','phNo','email','dateJoined','dateLeft']
        widgets = {
            'dateJoined': DateInput(),
            'dateLeft': DateInput(),
        }
        # widgets = {
        #     'name': forms.TextInput(attrs={'class': 'block'}),
        # }
    # dateLeft = DateField(widget=AdminDateWidget)

class editPropertyForm(ModelForm):
    class Meta:
        model = Properties
        fields = ['address','rent','propType','occupied']
        
    

# class transactionForm(ModelForm):
#     class Meta:
#         model = Transaction
#         fields = 

