from django.conf import settings

DEFAULT_SETTINGS = {
    'yandex_vrfy': '',
    'yandex_metrika_id': '',
    'google_vrfy': '',
    'google_analytics_id': '',
    'google_analytics_site': '',
    'alexa_vrfy': '',
}

USER_SETTINGS = getattr(settings, 'HTML5BASE_SETTINGS')
DEFAULT_SETTINGS.update(USER_SETTINGS)
