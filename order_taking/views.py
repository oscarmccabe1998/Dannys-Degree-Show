from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Order, starter, table


def index(request):
    orders = Order.objects.all()
    teststarter = starter.objects.all()
    #print(teststarter)
    #starter_query = starter.objects.raw("SELECT * FROM order_taking_starter WHERE table_number = 1")
    #test = table.objects.raw("SELECT * FROM order_taking_table WHERE auto_increment_id = 1")
    #for item in test:
    #    print(item)
    starts = []
    mains = []
    dessert = []
    order_list = []
    checkstart = []
    temp = ""
    temp1 = ""
    templist = []
    #values = " "
    x = 17
    template = loader.get_template('order_taking/index.html')
    #for order in range(x):
    #    checkstart = starter.objects.filter(table_number= order)
    #    print(checkstart)
    #    for q in checkstart:
    #        temp = ""
    #        starts.append(q.starters)
    #        table = q.table_number.table_number
    #        temp = temp + q.starters + ", "
    for order in range(x):
        temp = starter.objects.filter(table_number= order)
        y = len(temp)
        print(y)

        for test in temp:
            order_list.append(test.starters)
        print(order_list)
    for item in order_list:
        checkstart.append(item)
    print(checkstart)
        #order_list.append(checkstart.starters)

            #tablenum = table.objects.filter(table_number = table)
            #print(tablenum.table_number)
    #print(temp)
    #order1 = []
    
    #order1.append(starter.objects.filter(table_number = 1))
    #order_list.append(order1)
    #print(order_list)
    #print(starts)

    

        #query = Order.objects.raw("SELECT * FROM order_taking_Order WHERE table_number = %s AND waiting_for_service = FALSE", [order])
        #starter_query = Order.objects.raw("SELECT * FROM order_taking_starter WHERE table_number = %s", [order])
    #    starter_query = starter.objects.raw("SELECT table_number FROM order_taking_starter", translations=order_taking_table)
    #values=values+starts
    #print(values)
    #order_list.append(starts)

    #    for q in starter_query:
    #        starts.append(q)
            #order_list.append(q)
            #starts.append(q.starters)
            #mains.append(q.mains)
            #dessert.append(q.deserts)
        #for q in query:
        #    print(q.table_number)
            #print(q.starters)
        #    starts.append(q.starters)
    #    order_list.append(order)
    #order_list.append(starts)
    #order_list.append(mains)
    #order_list.append(dessert)

    #print(values)
    
    
    
    #print(order_list)
    context = {
        'order_list': order_list, 
        'starts': starts,
        'table': table,
        'checkstart': checkstart
    }
    #print(order_list)
    return render(request, 'order_taking/index.html', context)
    


def detail(request, order_id):
    return HttpResponse("You are looking at Order %S." % order_id)

