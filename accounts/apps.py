from django.apps import AppConfig


class AccountConfig(AppConfig):
    name = 'accounts'
    verbose_name = 'Profile'

    def ready(self):
        import accounts.signals
