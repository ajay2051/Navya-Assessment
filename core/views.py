from django.shortcuts import render
from django.views.generic import View
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

from core.models import InformationModel


# Create your views here.

def information(request):
    infos = InformationModel.objects.all()
    context = {
        "infos": infos
    }
    return render(request, 'core/main.html', context=context)


def html_to_pdf(template_src, context_dict):

    # Get Template which will be converted to PDF
    template = get_template('core/main.html')

    html = template.render(context_dict)
    result = BytesIO()

    # Convert the contents of template into PDF
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        # Getting all information data
        context = {
            "infos": InformationModel.objects.all()
        }

        # getting the template
        pdf = html_to_pdf('core/main.html', context)

        # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')


