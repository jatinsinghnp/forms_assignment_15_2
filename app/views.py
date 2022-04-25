from django.shortcuts import render, HttpResponseRedirect
from .forms import CrudForm
from .models import model1

# Create your views here.
def home(request):
    records = model1.objects.all()

    return render(request, "index.html", {"records": records})


def form_set(request):
    forms = CrudForm()

    return render(request, "set_form.html", {"forms": forms})


def get_form(request):
    id = request.GET.get("id")
    name = request.GET.get("name")
    address = request.GET.get("address")
    record = model1()
    record.name = name
    record.id = id
    record.adress = address
    record.save()

    return HttpResponseRedirect("/app/")


def delete_record(request):
    id = request.GET.get("id")

    record = model1.objects.get(id=id)
    record.delete()

    return HttpResponseRedirect("/app/")


def update_record(request):
    id = request.GET.get("id")
    record = model1.objects.get(id=id)
    forms = CrudForm(
        initial={"name": record.name, "id": record.id, "address": record.adress}
    )
    

    return render(
        request,
        "update.html",
        {
            
            "forms": forms,
        },
    )


def save_record(request):
    id = request.GET.get("id")
    name = request.GET.get("name")
    address = request.GET.get("address")
    record = model1.objects.get(id=id)
    record.name = name
    record.id = id
    record.adress = address
    record.save()

    return HttpResponseRedirect("/app/")
