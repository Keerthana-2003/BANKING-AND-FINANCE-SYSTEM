from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.forms import TextInput, EmailInput
from .models import Transaction
from django.forms.widgets import Select

class RegistrationData(UserCreationForm):
	password1 = forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'input', 'type':'password', 'align':'center', 'placeholder':'Password'}))
	password2 = forms.CharField(label="Confirm password",widget=forms.PasswordInput(attrs={'class':'input', 'type':'password', 'align':'center', 'placeholder':'Confirm Password'}))
	class Meta:
		model=User
		fields=['first_name','last_name','email','username']
		widgets={
		'first_name':forms.TextInput(attrs={'class':'input','placeholder':'FirstName'}),
		'last_name':forms.TextInput(attrs={'class':'input','placeholder':'LastName'}),
		'email':forms.EmailInput(attrs={'class':'input','placeholder':'Email'}),
		'username':forms.TextInput(attrs={'class':'input','placeholder':'UserName'}),

		}
class ContactData(UserCreationForm):
	class Meta1:
		model=User
		fields=['name','email','message']
		widgets={
			'name':forms.TextInput(attrs={'class':'form_item','placeholder':'Name'}),
			'email':forms.EmailInput(attrs={'class':'form_item','placeholder':'Email'}),
			'message':forms.TextInput(attrs={'class':'form_item','placeholder':'Message'}),
		}

class TransactionForm(forms.ModelForm):
    username=forms.CharField(widget=forms.HiddenInput())
    class Meta:
        model = Transaction
        fields = "__all__"
        widgets={
		'tran_date':forms.DateInput(attrs={'class':'input','placeholder':'MM/DD/YYYY'}),
		'tran_category':forms.TextInput(attrs={'class':'input','placeholder':'Ex: Bills'}),
		'credit_amount':forms.TextInput(attrs={'class':'input','placeholder':'Credit Amount'}),
		'debit_amount':forms.TextInput(attrs={'class':'input','placeholder':'Debit Amount'}),
		
		}
