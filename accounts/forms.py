from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Custom User Creation Form"""

    class Meta(UserCreationForm):
        """Dis Meta class."""

        # This is the Meta class. It contains information
        # about how to get an instance of the class created.
        # It is not common to use this, but Django does for
        # certain things. Like this.
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            "username",
            "age",
            "email",
            # No need for password as it is required
        )


class CustomUserChangeForm(UserChangeForm):
    """Custom User Change Form"""

    class Meta:
        """Dis meta"""

        model = CustomUser
        fields = (
            "username",
            "age",
            "email",
        )
