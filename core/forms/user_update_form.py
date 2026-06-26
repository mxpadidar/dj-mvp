from django.contrib.auth import get_user_model
from django.forms import ModelForm

User = get_user_model()


class ProfileUpdateForm(ModelForm):
    "Form for updating user profile information."

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
