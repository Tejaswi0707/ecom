from django.apps import AppConfig


class CartConfig(AppConfig): # to configure cart app
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cart'
