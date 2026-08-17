from django.apps import AppConfig



class ShoppingBagConfig(AppConfig):
    # Created with AI to merge guest and user baskets
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'shopping_bag'
    
    def ready(self):
        import shopping_bag.signals
