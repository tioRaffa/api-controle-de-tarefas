from decouple import config
from .environment import DEBUG
DJOSER = {
    'PASSWORD_RESET_CONFIRM_URL': 'password/reset/{uid}/{token}',
    'PASSWORD_CONFIRM_RETYPE': True
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='webmaster@localhost')

EMAIL_HOST = config('EMAIL_HOST', default='')
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=False, cast=bool)
EMAIL_USE_SSL = config('EMAIL_USE_SSL', default=False, cast=bool)