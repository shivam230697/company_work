from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .forms import IndexForm, RawMaterialForm, ProductionForm, LoginForm
from .models import RawMaterialModel, ProductionModel
from django.contrib import messages


def index(request):
    index_form = IndexForm()
    rm_form = RawMaterialForm()
    data = RawMaterialModel.objects.all()
    return render(request, "index.html", context={'form': index_form, 'rm_form': rm_form, 'data':data})


def base(request):
    return render(request, "base.html")


def raw_material(request):
    rm_form = RawMaterialForm()
    if request.method == 'POST':
        rm_form = RawMaterialForm(request.POST)
        if rm_form.is_valid():
            rst_f = rm_form.cleaned_data['rst_no']
            net_wt_f = rm_form.cleaned_data['net_wt']
            rate_f = rm_form.cleaned_data['rate']
            total_f = rm_form.cleaned_data['total']
            rm_model = RawMaterialModel()
            rm_model.rst_no, rm_model.net_wt, rm_model.rate, rm_model.total = rst_f, net_wt_f, rate_f, total_f
            rm_model.save()
        return render(request, "raw_material.html", context={'raw_material_form': RawMaterialForm()})
    if request.method == 'GET':
        return render(request, "raw_material.html", context={'raw_material_form': rm_form})


def raw_material_view(request):
    rm_data = RawMaterialModel.objects.all()
    return render(request, "rm_details.html", context={'rm_data': rm_data})


def raw_material_update(request, pk):
    update_data = RawMaterialModel.objects.get(id=str(pk))

    return render(request, "rm_update.html", context={'data': update_data})


def confirm(request, pk):
    data = RawMaterialModel.objects.get(id=str(pk))
    data.rst_no = request.POST.get("rst")
    data.net_wt = request.POST.get("net_wt")
    data.rate = request.POST.get("rate")
    data.total = request.POST.get("total")
    if request.method == "POST":
        data.save()
        messages.success(request, "updated entry")
    rm_data = RawMaterialModel.objects.all()
    return render(request, "rm_details.html", context={'rm_data': rm_data})


def delete_raw_material_entry(request, pk):
    remove_data = RawMaterialModel.objects.get(id=str(pk))
    remove_data.delete()
    rm_data = RawMaterialModel.objects.all()
    return render(request, "rm_details.html", context={'rm_data': rm_data})


def add_production(request):
    add_product_form = ProductionForm()
    if request.method == 'POST':
        product_form = ProductionForm(request.POST)
        if product_form.is_valid():
            product_rst = product_form.cleaned_data['product_rst']
            product_net_wt = product_form.cleaned_data['product_net_weight']
            product_vehicle_no = product_form.cleaned_data['vehicle_no']
            product_model = ProductionModel()
            product_model.product_rst, product_model.product_net_weight, product_model.vehicle_no, = (
                product_rst, product_net_wt, product_vehicle_no)
            product_model.save()
        return render(request, "add_production.html", context={'add_product': ProductionForm()})
    if request.method == 'GET':
        return render(request, "add_production.html", context={'add_product': add_product_form})
    return render(request, "add_production.html", context={'add_product': add_product_form})


def view_production(request):
    production_data = ProductionModel.objects.all()
    return render(request, "production_details.html", context={'production_data': production_data})


def edit_production(request, pk):
    edit_data = ProductionModel.objects.get(id=str(pk))
    print(edit_data)
    return render(request, "edit_production.html", context={'data': edit_data})


def update_production(request, pk):
    data = ProductionModel.objects.get(id=str(pk))
    data.product_rst = request.POST.get("product_rst")
    data.product_net_weight = request.POST.get("product_net_wt")
    data.vehicle_no = request.POST.get("vehicle_num")
    if request.method == "POST":
        data.save()
        messages.success(request, "updated entry")
    product_data = ProductionModel.objects.all()
    return render(request, "production_details.html", context={'production_data': product_data})


def delete_production(request, pk):
    remove_data = ProductionModel.objects.get(id=str(pk))
    remove_data.delete()
    production_data = ProductionModel.objects.all()
    return render(request, "production_details.html", context={'production_data': production_data})


def add_final_good(request):
    return HttpResponse("add final good")


def view_final_goods(request):
    return HttpResponse("view final good")


def update_final_good(request):
    return HttpResponse("update final good")


def delete_final_goods(request):
    return HttpResponse("delete final good")


# myapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user:
            login(request, user)
            return redirect('base')
        else:
            # Handle invalid login
            pass
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('base')


def user_signup(request):
    if request.method == 'POST':
        print("post method")
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("enter valid form")
            user = form.save()
            login(request, user)
            return redirect('base')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
