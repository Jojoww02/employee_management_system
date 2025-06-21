from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    total_gaji = forms.DecimalField(
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'tanggal_lahir': forms.DateInput(attrs={'type': 'date'}),
            'tanggal_bergabung': forms.DateInput(attrs={'type': 'date'}),
        }