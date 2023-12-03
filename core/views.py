from django.shortcuts import render

from core.models import InformationModel


# Create your views here.

def information(request):
    infos = InformationModel.objects.all()
    context = {
        "infos": infos
    }
    return render(request, 'core/main.html', context=context)
