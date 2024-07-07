from django.apps import AppConfig


class AutoserviceappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "autoserviceapp"

    def ready(self):
        from .signals import create_profile
