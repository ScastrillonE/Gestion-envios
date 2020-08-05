from io import BytesIO
from django.http import HttpResponse
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMessage

import os
from barcode.writer import ImageWriter
import barcode
import base64
import time

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


def render_to_pdf(template, data={}):
    template = get_template(template)
    html = template.render(data)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def generate_codebar(consecutivo):
    code = barcode.get('code128', consecutivo, writer=ImageWriter())
    filename = code.save('code128',{"module_width":0.35, "module_height":10, "font_size": 18, "text_distance": 1, "quiet_zone": 3})

    return filename


# def code_to_base64(consecutivo):
#     code = barcode.get('code128', consecutivo, writer=ImageWriter())
#     filename = code.save('code128')
#     image = open('code128.png', 'rb')
#     image_read = image.read()
#     codebar = base64.encodebytes(image_read)
#     codebar = str(codebar).split("'")
#     codebar[0] = 'data:image/png;base64,'
#     list(codebar)
#     codigobarra = codebar[0] + codebar[1]
#
#     remove("code128.png")
#     return codigobarra
