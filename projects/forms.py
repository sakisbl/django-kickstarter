from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name',
            'short_description',
            'description',
            'cover_image',
            'goal',
            'category',
            'finish',
        ]
        widgets = {
            'finish': forms.DateInput(attrs={'class': 'datepicker'})
        }

    def clean_goal(self, *args, **kwargs):
        goal = self.cleaned_data.get('goal')
        if goal > 10000000:
            raise forms.ValidationError('The maximum amount raised cannot exceed 100000000')
        return goal


class RaiseAmountForm(forms.Form):
    amount = forms.DecimalField()

    def clean_amount(self, *args, **kwargs):
        amount = self.cleaned_data.get('amount')
        if amount > 10000000:
            raise forms.ValidationError('You inserted a very big value')
        return amount
