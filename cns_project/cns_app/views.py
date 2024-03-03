from django.db.models import Sum
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .forms import IndexForm, RawMaterialForm, ProductionForm, LoginForm, InvoiceForm, PaymentForm, CustomerForm
from .models import RawMaterialModel, ProductionModel, InvoiceModel, PaymentModel, Customer
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from datetime import datetime
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.decorators import user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from num2words import num2words


def index(request):
    index_form = IndexForm()
    rm_form = RawMaterialForm()
    data = RawMaterialModel.objects.all()
    return render(request, "index.html", context={'form': index_form, 'rm_form': rm_form, 'data': data})


def base(request):
    return render(request, "base.html")


@login_required
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
            messages.success(request, "Successfully Added Raw Material")
        else:
            for errors in rm_form.errors.values():
                for error in errors:
                    messages.error(request, error)
            print(rm_form.errors)
            return render(request, "raw_material.html", context={'raw_material_form': RawMaterialForm()})
        return render(request, "raw_material.html", context={'raw_material_form': RawMaterialForm()})
    if request.method == 'GET':
        return render(request, "raw_material.html", context={'raw_material_form': rm_form})


@login_required
def raw_material_view(request):
    try:
        rm_data = RawMaterialModel.objects.all()
    except Exception as e:
        messages.error(request, e)
    return render(request, "rm_details.html", context={'rm_data': rm_data})


@user_passes_test(lambda user: user.is_superuser)
def raw_material_update(request, pk):
    try:
        update_data = RawMaterialModel.objects.get(id=str(pk))
    except Exception as error:
        messages.error(request, error)
    return render(request, "rm_update.html", context={'data': update_data})


@user_passes_test(lambda user: user.is_superuser)
def confirm(request, pk):
    data = None
    try:
        data = RawMaterialModel.objects.get(id=str(pk))
        data.rst_no = request.POST.get("rst")
        data.net_wt = request.POST.get("net_wt")
        data.rate = request.POST.get("rate")
        data.total = request.POST.get("total")
    except Exception as error:
        messages.error(request, error)
    if request.method == "POST":
        data.save()
        messages.success(request, "updated entry")

    rm_data = RawMaterialModel.objects.all()
    return render(request, "rm_details.html", context={'rm_data': rm_data})


@user_passes_test(lambda user: user.is_superuser)
def delete_raw_material_entry(request, pk):
    try:
        remove_data = RawMaterialModel.objects.get(id=str(pk))
        deleted_rst = remove_data.rst_no
        remove_data.delete()
        messages.success(request, str(deleted_rst) + " Data Deleted Successfully")

    except Exception as error:
        messages.error(request, error)
    rm_data = RawMaterialModel.objects.all()
    return render(request, "rm_details.html", context={'rm_data': rm_data})


@login_required
def add_production(request):
    add_product_form = ProductionForm()
    if request.method == 'POST':

        product_form = ProductionForm(request.POST)
        if product_form.is_valid():
            product_rst = product_form.cleaned_data['product_rst']
            product_net_wt = product_form.cleaned_data['product_net_weight']
            product_vehicle_no = product_form.cleaned_data['vehicle_no'] or 'UNKNOWN'
            product_model = ProductionModel()
            product_model.product_rst, product_model.product_net_weight, product_model.vehicle_no, = (
                product_rst, product_net_wt, product_vehicle_no.upper())
            product_model.save()
            messages.success(request, "Production added successfully")
        else:
            for errors in product_form.errors.values():
                for error in errors:
                    messages.error(request, error)
                print(product_form.errors)
            return render(request, "add_production.html", context={'add_product': ProductionForm()})
    if request.method == 'GET':
        return render(request, "add_production.html", context={'add_product': add_product_form})
    return render(request, "add_production.html", context={'add_product': add_product_form})


@login_required
def view_production(request):
    production_data = ProductionModel.objects.all()
    return render(request, "production_details.html", context={'production_data': production_data})


@user_passes_test(lambda user: user.is_superuser)
def edit_production(request, pk):
    try:
        edit_data = ProductionModel.objects.get(id=str(pk))
    except Exception as error:
        messages.error(request, error)
    return render(request, "edit_production.html", context={'data': edit_data})


@user_passes_test(lambda user: user.is_superuser)
def update_production(request, pk):
    data = None
    try:
        data = ProductionModel.objects.get(id=str(pk))
        data.product_rst = request.POST.get("product_rst")
        data.product_net_weight = request.POST.get("product_net_wt")
        data.vehicle_no = request.POST.get("vehicle_num")
    except Exception as error:
        messages.error(request, error)
    if request.method == "POST":
        data.save()
        messages.success(request, "updated entry")
    product_data = ProductionModel.objects.all()
    return render(request, "production_details.html", context={'production_data': product_data})


@user_passes_test(lambda user: user.is_superuser)
def delete_production(request, pk):
    try:
        remove_data = ProductionModel.objects.get(id=str(pk))
        deleted_rst = remove_data.product_rst
        remove_data.delete()
        messages.success(request, str(deleted_rst) + " Data Deleted Successfully")
    except Exception as error:
        messages.error(request, error)
    production_data = ProductionModel.objects.all()
    return render(request, "production_details.html", context={'production_data': production_data})


@login_required
def add_invoice(request):
    from .models import Customer
    if request.method == "GET":
        invoice_form = InvoiceForm()
        return render(request, "add_invoice.html", {'invoice_form': invoice_form})
    elif request.method == 'POST':

        invoice_form = InvoiceForm(request.POST)

        if invoice_form.is_valid():
            invoice_model = InvoiceModel()
            invoice_model.customer = invoice_form.cleaned_data['customer']
            invoice_model.item_45mm = invoice_form.cleaned_data['item45mm']
            invoice_model.item_90mm = invoice_form.cleaned_data['item90mm']
            invoice_model.item_pencil = invoice_form.cleaned_data['item_pencil']
            invoice_model.item_45mm_quantity = invoice_form.cleaned_data['quantity_item1'] or 0
            invoice_model.item_90mm_quantity = invoice_form.cleaned_data['quantity_item2'] or 0
            invoice_model.item_pencil_quantity = invoice_form.cleaned_data['quantity_item3'] or 0
            invoice_model.item_45mm_rate = invoice_form.cleaned_data['price_item1'] or 0
            invoice_model.item_90mm_rate = invoice_form.cleaned_data['price_item2'] or 0
            invoice_model.item_pencil_rate = invoice_form.cleaned_data['price_item3'] or 0
            invoice_model.total_45mm = invoice_model.item_45mm_quantity/1000 * invoice_model.item_45mm_rate
            invoice_model.total_90mm = invoice_model.item_90mm_quantity/1000 * invoice_model.item_90mm_rate
            invoice_model.total_pencil = invoice_model.item_pencil_quantity/1000 * invoice_model.item_pencil_rate
            invoice_model.shipping_address = invoice_form.cleaned_data['shipping_address']
            invoice_model.shipping_state = invoice_form.cleaned_data['shipping_state']
            invoice_model.shipping_city = invoice_form.cleaned_data['shipping_city']
            invoice_model.shipping_zip_code = invoice_form.cleaned_data['shipping_zip_code']
            invoice_model.total = invoice_form.cleaned_data['total']
            invoice_model.gst = invoice_form.cleaned_data['gst']
            invoice_model.discount = invoice_form.cleaned_data['discount'] or 0
            invoice_model.payment = invoice_form.cleaned_data['payment']
            invoice_model.driver_name = invoice_form.cleaned_data['driver_name']
            invoice_model.driver_number = invoice_form.cleaned_data['driver_number']
            invoice_model.assigned_vehicle = invoice_form.cleaned_data['assigned_vehicle']
            invoice_model.paid_amount = invoice_form.cleaned_data['paid_amount']
            if invoice_model.paid_amount > invoice_model.payment:
                messages.error(request, 'Enter valid paid amount')
                return render(request, "add_invoice.html", {'invoice_form': InvoiceForm()})

            customer_model = Customer.objects.get(pk=invoice_form.cleaned_data['customer'].id)

            customer_model.payment_dues = (customer_model.payment_dues +
                                           invoice_form.cleaned_data['payment'] - invoice_model.paid_amount)
            customer_model.payment_status = 'PENDING'
            customer_model.save()
            invoice_model.save()
            messages.success(request, "Invoice Added Successfully")
        else:
            messages.error(request, invoice_form.errors)

        return render(request, "add_invoice.html", context={'invoice_form': InvoiceForm()})
    return render(request, "add_invoice.html", {'invoice_form': InvoiceForm()})


@login_required
def view_invoices(request):
    invoice_model = InvoiceModel.objects.all()
    return render(request, "view_invoices.html", {'invoice_data': invoice_model})


@user_passes_test(lambda user: user.is_superuser)
def update_final_good(request):
    return HttpResponse("update final good")


@user_passes_test(lambda user: user.is_superuser)
def delete_final_goods(request):
    return HttpResponse("delete final good")


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "Invalid user")
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('base')


@user_passes_test(lambda user: user.is_superuser)
def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('base')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def dashboard(request):
    if request.method == "POST":
        button_name = request.POST.get('report_button', None)
        result = True if button_name == "show production report" else False
        if button_name == "show production report":
            start_date = request.POST.get('from_date', None)
            last_date = request.POST.get('to_date', None)
            try:
                p_data = ProductionModel.objects.raw(
                    "select * from cns_app_productionmodel where  DATE(created_at) between %s and %s",
                    [start_date, last_date])
            except Exception as error:
                messages.error(request, error)

            table_name = ProductionModel._meta.db_table

            return render(
                request,
                'dashboard.html',
                {
                    'data': list(p_data),
                    'btn_name': button_name,
                    'from_date': start_date,
                    'to_date': last_date
                }
            )
        if button_name == "show raw material report":
            start_date = request.POST.get('from_date', None)
            last_date = request.POST.get('to_date', None)
            try:
                data = RawMaterialModel.objects.raw(
                    "select * from cns_app_rawmaterialmodel where "
                    " DATE(created_at) between %s and %s", [start_date, last_date])
            except Exception as error:
                messages.error(request, error)

            table_name = RawMaterialModel._meta.db_table

            a = list(data)
            return render(
                request,
                'dashboard.html',
                {
                    'data': list(data),
                    'btn_name': button_name,
                    'from_date': start_date,
                    'to_date': last_date
                }
            )

    return render(request, 'dashboard.html', {'data': '', 'btn_name': "button_name"})


def my_page(request):
    messages.info(request, "uploaded successfully")
    return render(request, "my_page.html")


@login_required
def add_customer(request):
    if request.method == "POST":
        customer_form = CustomerForm(request.POST or None)

        if customer_form.is_valid():
            customer_model = Customer()
            customer_model.customer_name = customer_form.cleaned_data['customer_name']
            customer_model.customer_number = customer_form.cleaned_data['customer_number']
            customer_model.customer_address = customer_form.cleaned_data['customer_address']
            customer_model.customer_state = customer_form.cleaned_data['customer_state']
            customer_model.customer_city = customer_form.cleaned_data['customer_city']
            customer_model.zip_code = customer_form.cleaned_data['zip_code']
            customer_model.customer_gstin = customer_form.cleaned_data['customer_gstin'].upper()

            customer_model.payment_dues = 0
            customer_model.payment_status = 'PAID'
            customer_model.save()
            messages.success(request, 'Successfully Customer added')
        else:
            messages.error(request, 'Customer Form is not submitted')
        return render(request, 'add_customer.html', {'customer_form': CustomerForm()})

    if request.method == "GET":
        return render(request, 'add_customer.html', {'customer_form': CustomerForm()})
    return render(request, 'add_customer.html', {'customer_form': CustomerForm()})


@login_required
def view_customer(request):
    customer_list = Customer.objects.all()
    return render(request, 'customer_list.html', {'customer_list': customer_list})


@login_required
def payment(request):
    payment_form = PaymentForm()
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)
        if payment_form.is_valid():
            payment_model = PaymentModel()
            payment_model.customer = payment_form.cleaned_data['customer']
            payment_model.payment_method = payment_form.cleaned_data['payment_method']
            payment_model.payment_amount = payment_form.cleaned_data['payment_amount']

            customer_model = Customer.objects.get(pk=payment_form.cleaned_data['customer'].id)
            if customer_model.payment_dues > payment_form.cleaned_data['payment_amount']:
                customer_model.payment_dues = customer_model.payment_dues - payment_form.cleaned_data['payment_amount']
                customer_model.payment_status = 'PENDING'
                customer_model.save()
            else:
                customer_model.payment_dues = 0
                customer_model.payment_status = 'PAID'
                customer_model.save()
                return render(request, "payment.html", {'payment_form': payment_form})
            payment_model.save()
            messages.success(request, "Payment done Successfully")
            # payment_model.payment_status = payment_form.cleaned_data['payment_status']

            # payment_model_data = PaymentModel.objects.filter(customer__id=payment_form.cleaned_data['customer'].id)
            # total_paid = payment_model_data.aggregate(payment_amount=Sum('payment_amount'))['payment_amount'] or 0
            # total_paid = total_paid + payment_form.cleaned_data['payment_amount']
            # fg_model_data = FinalGoods.objects.filter(customer__id=payment_form.cleaned_data['customer'].id)
            # total_amount = fg_model_data.aggregate(payment=Sum('payment'))['payment'] or 0
            # if total_paid < total_amount:
            #     payment_model.payment_dues = total_amount-total_paid
            #     payment_model.payment_status = 'pending'
            #     payment_model.save()
            # else:
            #     payment_model.payment_dues = 0
            #     payment_model.payment_status = 'paid'
            #     payment_model.save()

    return render(request, "payment.html", {'payment_form': payment_form})


@login_required
def view_payment(request):
    payments = PaymentModel.objects.all()
    return render(request, "payment_view.html", context={'payments': payments})


@login_required
def view_invoice(request, invoice_id):
    try:
        invoice = InvoiceModel.objects.get(pk=invoice_id)
        customer = Customer.objects.get(pk=invoice.customer.id)
        integer_part = int(invoice.payment)
        decimal_part = invoice.payment - int(invoice.payment)

        words_payment = num2words(integer_part).capitalize() + " Rupees & " + num2words(decimal_part*100).capitalize() + " Paise"
        return render(request, 'view_invoice.html',
                      {'invoice': invoice, 'customer': customer, 'words_payment': words_payment})

    except:

        messages.info(request, "invoice data not found")
        return render(request, 'view_invoice.html')
    return render(request, 'view_invoice.html')


def payment_history(request, customer_id):
    customer = Customer.objects.get(pk=customer_id)
    customer_invoices = InvoiceModel.objects.filter(customer=customer)
    customer_payments = PaymentModel.objects.filter(customer=customer)
    invoice_total = sum(i_payments.payment for i_payments in customer_invoices)
    paid_total = sum(c_payments.payment_amount for c_payments in customer_payments)
    remaining_amount = invoice_total - paid_total

    return render(
        request,
        'customer_payment_history.html',
        {
            'customer': customer,
            'customer_invoices': customer_invoices,
            'customer_payments': customer_payments,
            'invoice_total': invoice_total,
            'paid_total': paid_total,
            'remaining_amount': remaining_amount
        }
    )
