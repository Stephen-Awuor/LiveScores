from django import forms
from django.contrib.auth.models import User

class AdminProfileForm(forms.ModelForm):
    # extra password fields
    old_password = forms.CharField(widget=forms.PasswordInput, required=False, label="Old password")
    new_password = forms.CharField(widget=forms.PasswordInput, required=False, label="New password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, required=False, label="Confirm new password")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username']  # include username if you want

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_password = cleaned_data.get("confirm_password")

        if new_password or confirm_password:
            if new_password != confirm_password:
                raise forms.ValidationError("New passwords do not match.")
            if len(new_password) < 8:
                raise forms.ValidationError("New password must be at least 8 characters long.")
        return cleaned_data
