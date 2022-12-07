from django import template
from ..models import BookStatus
register = template.Library()


def availability(data):
    d = BookStatus.objects.filter(book__book_id__exact=data).order_by('-return_date').first()
    if d:
        return d.return_date

    else:
        return


register.filter('check', availability)