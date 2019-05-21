from django.apps import AppConfig
from .signals import create_profile, save_profile


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = 'profile'

    def ready(self):
        import users.signals
