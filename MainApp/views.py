from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from MainApp.models import call_reasons, call_actions, _approvals
from django.utils import timezone
from datetime import timedelta
from django.db.models import Count
from .models import *
from .forms import *

#Entry page view
def index(request):
    return render(request, 'index.html')


#Main page after login
def login_view(request):
    if request.method == "POST":
        user_type = request.POST["user_role"]
        username = request.POST["username"]
        password = request.POST["password"]
    try:
        get_user_data = UsersModel.objects.get(username=username, password=password, user_type=user_type)
        if get_user_data.user_type == 'Admin':
            get_products = ProductsModel.objects.filter()
            return render(request, 'admin.html',{'products_list':get_products})
        else:
            get_data = CallLogsModel.objects.filter(agent_idno=get_user_data.id)
            return render(request, 'agent.html', {'data':get_data})
    except UsersModel.DoesNotExist:
        return HttpResponse("<center><br><h3>User Does Not Exist</h3></center>")
  

#Add new product view for admin
def create_product(request):
    if request.method == "POST":
        product_name = request.POST["product_name"]
        product_type = request.POST["product_type"]
        customer_name = request.POST["customer_name"]
        address = request.POST["address"]
        mobile_no = request.POST["mobile_no"]
        region = request.POST["region"]
    post_data = ProductsModel.objects.create(product_name=product_name,product_type=product_type, customer_name=customer_name, address=address, mobile_no=mobile_no, region=region)
    get_products = ProductsModel.objects.filter()
    return HttpResponse("<center><h3>New Product has been added !</h3></center>")


def update_product(request):
    if request.method == "POST":
        serial_no = request.POST["serial_no"]
        update_data = ProductsModel.objects.get(serial_no=serial_no)
        form = ProductModelForm(request.POST, instance = update_data)  
        if form.is_valid():  
            form.save()  
    return HttpResponse("<center><h3>One Product has been updated !</h3></center>")


def delete_product(request,pk):
    ProductsModel.objects.get(id=pk).delete() 
    return HttpResponse("<center><h3>One Product has been deleted !</h3></center>")


#update view call by agent
def update_call_view(request):
    get_serial_nos = ProductsModel.objects.values_list('serial_no', flat=True)
    get_phone_nos = ProductsModel.objects.values_list('mobile_no', flat=True)
    get_all_products = ProductsModel.objects.all()
    get_all_call_logs = CallLogsModel.objects.all()

    #get model choices into lists
    list_call_reasons = [i[0] for i in call_reasons]
    list_call_actions = [i[0] for i in call_actions]
    list_approvals = [i[0] for i in _approvals]

    return render(request, 'updatecall.html', 
    {'sr_no':get_serial_nos, 
    'phone_no':get_phone_nos, 
    'get_all_products':get_all_products,
    'get_all_call_logs':get_all_call_logs,
    'get_call_reason':list_call_reasons,
    'list_call_actions':list_call_actions,
    'list_approvals':list_approvals})


#add call log
def add_new_call_log(request):
    if request.method == "POST":
        agent_idno = request.POST["agent_idno"]
        serial_no = request.POST["serial_no"]
        mobile_no = request.POST["mobile_no"]
        call_reason = request.POST["selected_items"]
        remark = request.POST["remark"]
        items = request.POST["product_name"]
        call_action = request.POST["selected_action"]
        approval = request.POST["selected_approval"]
        call_date = timezone.now().date()
    post_data = CallLogsModel.objects.create(
        agent_idno=agent_idno,
        serial_no=serial_no,
        mobile_no=mobile_no,
        call_reason=call_reason,
        remark=remark,
        items=items,
        call_action=call_action,
        approval=approval,
        call_date=call_date)

    return HttpResponse("<center><h3> Call log submitted !</h3></center>")

#get call logs
def get_call_logs(request):
    #get call logs for last two days
    date_before_two_days = timezone.now().date() - timedelta(days=2)
    try:
        get_call_logs = CallLogsModel.objects.filter(call_date__gte= date_before_two_days)
    except UsersModel.DoesNotExist:
        get_call_logs = ""
    return render(request, 'calllogs.html', {'call_logs':get_call_logs})


def get_call_reports(request):
    total_call = CallLogsModel.objects.all().count()
    count_by_date = CallLogsModel.objects.all().values('call_date').annotate(total=Count('call_date')).order_by('call_date')
    count_by_items = CallLogsModel.objects.all().values('items').annotate(total=Count('items')).order_by('items')
    count_by_call_reason = CallLogsModel.objects.all().values('call_reason').annotate(total=Count('call_reason')).order_by('call_reason')
    return render(request, 'reports.html', {'total_call':total_call, 'cbd':count_by_date, 'cbi':count_by_items, 'cbr':count_by_call_reason})

