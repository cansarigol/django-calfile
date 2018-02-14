import datetime
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

def convert_date(date_str):
    if not date_str:
        raise KeyError(_("Date parameter is missing!"))

    try:
        return datetime.datetime.strptime(date_str, settings.CALFILE_DF)
    except ValueError:
        raise ValueError(_(f"Could not convert parameter to date! data:{date_str}, format:{settings.CALFILE_DF}"))

    return None