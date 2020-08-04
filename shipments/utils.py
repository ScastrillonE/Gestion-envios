from io import BytesIO
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage

from xhtml2pdf import pisa


from customers.models import Customer
from company.models import CompanySettings


def send_email(name, email, number, shipping_company, send_date):
    body = render_to_string(
        'shipments/email_content.html', {
            'company': CompanySettings.objects.get(id=1),
            'name': name,
            'shipping_number': number,
            'shipping_company': shipping_company,
            'send_date': send_date,
        }
    )
    email_message = EmailMessage(
        subject='Confirmacion de pedido',
        body=body,
        from_email='{}'.format(CompanySettings.objects.get(id=1).get_email()),
        to=[email]
    )
    email_message.content_subtype = 'html'
    email_message.send()


def get_name(id):
    id = Customer.objects.get(id=id)
    return id.name


def render_to_pdf(template,data={}):
    template= get_template(template)
    html = template.render(data)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type='application/pdf')
    return None
