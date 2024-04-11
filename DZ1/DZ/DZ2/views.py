from django.core.paginator import Paginator
from django.shortcuts import render
from DZ2.models import Userss,Orders,Products
from DZ2.forms import UserForm
import datetime as DT   
from django.db.models import Q


def orders (request, user_id=1):
    if request.method=='POST':
        today = DT.date.today()
        week_ago = today - DT.timedelta(days=7)
        month_ago = today - DT.timedelta(days=31)
     
        year_ago = today - DT.timedelta(days=365)
        
        form=UserForm(data=request.POST)
        radio=request.POST['radio']
        
        if radio=="month":
            orders=Orders.objects.filter(Q(user_id=user_id),Q(date_create__gte=month_ago)).select_related("product")
           
        elif radio=="year":
            orders=Orders.objects.filter(Q(user_id=user_id),Q(date_create__gte=year_ago)).select_related("product")
           
        else:
           
            orders=Orders.objects.filter(Q(user_id=user_id),Q(date_create__gte=week_ago)).select_related("product")
            
   
    context={
        "orders": orders
    }
    return render(request,'DZ2/orders.html',context)

