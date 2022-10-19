from django.apps import AppConfig
from django.core.checks import Tags, register

from django_google_recaptcha.checks import recaptcha_key_check


class CaptchaConfig(AppConfig):
    name = "django_google_recaptcha"
    verbose_name = "Django reCAPTCHA"

    def ready(self):
        register(recaptcha_key_check, Tags.security)