from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    # Code generated with AI to record password reset requests.
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
    
    def ready(self):
        # Registers the signals
        import profiles.signals
    # End of AI generated code.
