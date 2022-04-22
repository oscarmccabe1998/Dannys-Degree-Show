from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Order


def index(request):
    orders = Order.objects.all()
    starts = []
    mains = []
    dessert = []
    order_list = []
    x = 17
    template = loader.get_template('order_taking/index.html')
    for order in range(x):
        query = Order.objects.raw("SELECT * FROM order_taking_Order WHERE table_number = %s AND waiting_for_service = FALSE", [order])
        for q in query:
            #order_list.append(q)
            starts.append(q.starters)
            mains.append(q.mains)
            dessert.append(q.deserts)
        #for q in query:
        #    print(q.table_number)
            #print(q.starters)
        #    starts.append(q.starters)
        order_list.append(order)
    order_list.append(starts)
    order_list.append(mains)
    order_list.append(dessert)
    print(starts)
    print(mains)
    print(dessert)
    #print(order_list)
    context = {
        'order_list': order_list
    }
    #print(order_list)
    return render(request, 'order_taking/index.html', {"order_list": order_list})
    


def detail(request, order_id):
    return HttpResponse("You are looking at Order %S." % order_id)

