from django.shortcuts import render
from django_datatables_view.base_datatable_view import BaseDatatableView
from . models import *
from django.shortcuts import render

from django.utils.html import escape
from . models import Employee

# Create your views here.from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import escape


class OrderListJson(BaseDatatableView):
    model = Employee
    columns = ['dob', 'phone_number', 'joining_date', 'address']
    order_columns = ['dob', 'phone_number', 'joining_date', 'address']
    max_display_length = 10

    def render_column(self, row, column):
        if column == 'address':
            
            return row.address+' '+row.address
        else:
            return super(OrderListJson, self).render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        
        if search:
            qs = qs.filter(address__istartswith=search)
       
        return qs
    


def view_project(request):

    return render(request,'check/check1.html')