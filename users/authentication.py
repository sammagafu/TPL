from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

User = get_user_model()

class EmailOrUsernameOrPhoneBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Try logging in with username
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            # Try logging in with email
            try:
                user = User.objects.get(email=username)
            except User.DoesNotExist:
                # Try logging in with phone number
                try:
                    user = User.objects.get(phone_number=username)
                except User.DoesNotExist:
                    return None

        if user.check_password(password):
            return user
        return None