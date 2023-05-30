
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt
from .models import CustomerData
import csv
from django.db import models
from django.db.models import Count,Sum,Max


# Create your views here.
def table(request):
    unique_customers=CustomerData.objects.values('customer_Id').annotate(frequent_modes_of_transanction=Max('mode_of_payments'))
    # For TABLE
    customer = []
    values = []
    for item in unique_customers:
        customer.append(item['customer_Id'])
        values.append(item['frequent_modes_of_transanction'])

    response_data = {
            "customer" : customer,
            "values" :values
        }
    # Return the JSON response
    return JsonResponse(response_data)



@csrf_exempt
def analytics(request):
    if request.method == "GET":
        type = request.GET.get('type')
        if type == "table":
            response = table(request)
            return response
        else:
            return HttpResponse("WOW")
    else:
        return HttpResponse("WOW")
    

def index(request):
    return HttpResponse("index")