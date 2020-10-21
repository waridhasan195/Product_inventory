from django import forms 
from .models import Computer, Operating_system
from django.forms import ModelForm 

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['computer_name', 'operating_system', 'IP_address', 'MAC_address', 'user_name', 'location', 'purchase_date']

    def clean_computer_name(self):
            # Validates the Computer Name Field
        computer_name = self.cleaned_data.get('computer_name')
        if (computer_name == ""):
            raise forms.ValidationError('This field cannot be left blank')

        for instance in Computer.objects.all():
            if instance.computer_name == computer_name:
                raise forms.ValidationError(computer_name + ' is already added')
            print("Already added")
        return computer_name

    

class ComputerSearchForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['user_name','export_to_CSV']

