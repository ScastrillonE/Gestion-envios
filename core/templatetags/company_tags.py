from django import template
from company.models import CompanySettings

register = template.Library()

@register.simple_tag
def company_data():
    try:
        company = CompanySettings.objects.get(id=1)
        return company
    except :

        company = 'Default'
        return company