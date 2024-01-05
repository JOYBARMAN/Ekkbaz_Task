from django.db.models import TextChoices


class OtpType(TextChoices):
    REGISTRATION = "REGISTRATION", "Registration"
    LOGIN = "LOGIN", "Login"
    UNDEFINED = "UNDEFINED", "Undefined"
