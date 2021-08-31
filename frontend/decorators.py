from views_log.models import ViewLog
from geolite2 import geolite2

reader = geolite2.reader()


def track_views(function):
    def wrap(request, *args, **kwargs):
        ip = ""
        x_forward_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forward_for:
            ip = x_forward_for.split(',')[0]
        else:
            ip = request.META['REMOTE_ADDR']

        match = reader.get(ip)
        country = ""
        referer = ""
        if match:
            country = match['country']['names']['en']

        if 'HTTP_REFERER' in request.META:
            referer = request.META['HTTP_REFERER']

        log = ViewLog(ip=ip,
                      agent=request.META['HTTP_USER_AGENT'],
                      host=request.META['HTTP_HOST'],
                      url=request.build_absolute_uri(),
                      referer=referer,
                      country=country)

        log.save()

        return function(request, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
