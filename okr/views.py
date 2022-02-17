from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Okr
from django.template import loader
from .forms import OkrForm


def okr_register(request):
    if request.method == 'POST':
        form = OkrForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('okr_list')
    form = OkrForm()
    return render(request, 'okr_register/register.html', {'form': form})


def okr_list(request):
    okrs = Okr.objects.all()
    template = loader.get_template('okr_list/list.html')
    context = {
        'okrs': okrs
    }
    return HttpResponse(template.render(context, request))


def okr_view(request, id):
    okr = get_object_or_404(Okr, pk=id)
    template = loader.get_template('okr_view/okr.html')
    context = {
        'okr': okr
    }
    return HttpResponse(template.render(context, request))

