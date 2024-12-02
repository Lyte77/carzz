from django.apps import AppConfig


class CarzzConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'carzz'

    def ready(self):
        import carzz.signals
