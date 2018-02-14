import datetime
import vobject
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from .utils import convert_date

@require_http_methods(["POST"])
def calfile(request):
    start_date = convert_date(request.POST.get("start_date", ""))
    end_date = convert_date(request.POST.get("end_date", ""))
    summary = request.POST.get("summary", "Summary")
    filename = request.POST.get("filename", "calfile")

    cal = vobject.iCalendar()
    cal.add('method').value = 'PUBLISH'
    vevent = cal.add('vevent')
    vevent.add('dtstart').value = start_date
    vevent.add('dtend').value = end_date
    vevent.add('summary').value = summary
    vevent.add('uid').value = '1'
    vevent.add('dtstamp').value = datetime.datetime.now()

    icalstream = cal.serialize()
    response = HttpResponse(icalstream)
    response['Content-Disposition'] = f"attachment; filename={filename}.ics"
    return response
