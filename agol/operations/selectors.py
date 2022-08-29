from django.db.models.query import QuerySet
from django.db.models import Prefetch, Count, Q
from operations.models import SafetyChecklist
from customers.models import Order
from django.shortcuts import get_object_or_404



def order_list(order_status) -> QuerySet[Order]:
    return(Order.objects.filter(order_status=order_status))

def checklist_details_list() -> QuerySet[SafetyChecklist]:
    safety_list=[]
    safety_orders = SafetyChecklist.objects.all().values('order_id').distinct()
    for index in range(len(safety_orders)):
        slist=list(safety_orders[index].values())
        safety_list.append(slist)
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
    print(flat_list)
    return(Order.objects.filter(id__in=flat_list).select_related())
    # Blog.objects.filter(pk__in=[1, 4, 7])
#     return()
#     return(SafetyChecklist.objects.all().select_related().prefetch_related(
#             Prefetch('order_id',
#             queryset=Order.objects.all())
#         )
# )

def checklist_details(pk) -> QuerySet[SafetyChecklist]:
    return(SafetyChecklist.objects.filter(order_id=pk).select_related())

    return(SafetyChecklist.objects.filter(personscore_set__name="Bob").prefetch_related("personscore_set"))
