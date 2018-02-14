from django.conf import settings

CALFILE_DF = getattr(settings, 'CALFILE_DATE_FORMAT', '%d-%m-%Y %H:%M')
