from django.db.models.query import QuerySet
from django.db.models import Prefetch, Count, Q
from operations.models import SafetyChecklist, Labinspection
from customers.models import Order
from django.shortcuts import get_object_or_404

def get_order(pk):
    return get_object_or_404(Order, id=pk)


def order_list(order_status) -> QuerySet[Order]:
    return(Order.objects.filter(order_status=order_status))

def checklist_details_list() -> QuerySet[SafetyChecklist]:
    safety_list=[]
    safety_orders_objs = SafetyChecklist.objects.all().values('order_id').distinct()
    for index in range(len(safety_orders_objs)):
        id_list=list(safety_orders_objs[index].values())
        safety_list.append(id_list)
    flat_list = [item for sublist in safety_list for item in sublist]
    '''
    https://stackoverflow.com/
    questions/952914/how-do-i-
    make-a-flat-list-out-of-a-
    list-of-lists

    Given a list of lists l,
    flat_list = []
    for sublist in l:
        for item in sublist:
            flat_list.append(item)
        '''    
    return(Order.objects.filter(id__in=flat_list).select_related())


def checklist_details(pk) -> QuerySet[SafetyChecklist]:
    return(SafetyChecklist.objects.filter(order_id=pk).select_related())

    return(SafetyChecklist.objects.filter(personscore_set__name="Bob").prefetch_related("personscore_set"))

def labinspection_details(pk) -> QuerySet[Labinspection]:
    
    return(Labinspection.objects.filter(order_id=pk))
