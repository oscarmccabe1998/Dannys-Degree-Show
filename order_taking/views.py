from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Order, starter, table
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

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
    #check = Order.objects.filter(pending=False).count()
    #if check < 6:
    #    Order.objects.filter
    #print(check)
    query = Order.objects.filter(pending=False)
    for q in query:
        order_list.append(q)
    #for order in range(x):
        #temp1 = ""
        #temp = starter.objects.filter(table_number= order)
    #    query = Order.objects.filter(table_number=order)
     #   print(query)
      #  for q in query:
       #     print(q)
            #if q.filter(waiting_for_service = False):
        #    order_list.append(q)
        #y = len(temp)
        #print(y)

        #for test in temp:
        #    order_list.append(test.starters)
        #    for order in order_list:
        #        temp1 = order + ", "
               
        #    starts.append(temp1)


        #print(order_list)
        #    print(temp1)
        #    checkstart.append(starts)
    #for item in order_list:
    #    checkstart.append(item)
    #print(checkstart)
        #order_list.append(checkstart.starters)

            #tablenum = table.objects.filter(table_number = table)
            #print(tablenum.table_number)
    #print(temp)
    #order1 = []
    #print(starts)
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
    
def update_starter(request, table_number):
    starter = Order.objects.get(pk=table_number)
    response = Order.objects.filter(pk = table_number).update(starter_ready=True)
    return redirect(index)

def update_main(request, table_number):
    main = Order.objects.get(pk=table_number)
    response = Order.objects.filter(pk = table_number).update(mains_ready=True)
    return redirect(index)

def update_desert(request, table_number):
    desert = Order.objects.get(pk=table_number)
    response = Order.objects.filter(pk = table_number).update(deserts_ready=True)
    return redirect(index)

