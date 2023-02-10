from django.apps import AppConfig


class AnecdoteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'anecdote'
    verbose_name = 'Анегдоти'
