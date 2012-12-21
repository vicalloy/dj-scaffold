from base import *

DEBUG = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#devserver
try:
    import devserver
    INSTALLED_APPS += ('devserver',)
    MIDDLEWARE_CLASSES += ('devserver.middleware.DevServerMiddleware',)
    INSTALLED_APPS = ('devserver',) + INSTALLED_APPS#devserver must in first
except Exception, e:
    pass

#debug_toolbar
try:
    import debug_toolbar
    INSTALLED_APPS += ('debug_toolbar',)
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INTERNAL_IPS = ('127.0.0.1',)
except Exception, e:
    pass
