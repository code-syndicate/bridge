from django.conf import settings

def URLContextProcessor(request):
    path = None
    if settings.DEBUG:
        path = 'http://127.0.0.1:8000/'

    else:
        path = request.META.get('HTTP_HOST')

    return {

        'host' : path,

    }
