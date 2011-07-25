from django.conf import settings

DEFAULT_SETTINGS = {
}

USER_SETTINGS = getattr(settings, 'HTML5BASE_SETTINGS')
DEFAULT_SETTINGS.update(USER_SETTINGS)


globals().update(DEFAULT_SETTINGS)
