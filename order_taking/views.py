from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Order, starter, table
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
import time
import datetime

def index(request):
    order_list = []
    waiting = []
    test = '0'
    ready = Order.objects.filter(waiting_for_service=True)
    for dish in ready:
        if dish.served==False:
            waiting.append(dish)
            if dish.waiting_for_service==True:
                #return redirect(index)
                print(waiting)
    ready_query = Order.objects.filter(pending=False)
    ready_query2 = Order.objects.filter(waiting_for_service=True)
    for dish2 in ready_query2:
        if dish2:
        #time.sleep(2)
            if dish2.served==False:
                table_number = dish2.table_number
                Order.objects.filter(pk=table_number).update(served=True)
                total_seconds = 1
                while total_seconds > 0:
                    timer = datetime.timedelta(seconds = total_seconds)
                    print(timer, end="/r")
                    time.sleep(1)
                    total_seconds -= 1
                check = Order.objects.filter(pending=True).count()
                new_order_list = []
                if check < 0:
                    pass
                if Order.objects.filter(pending=True):
        
                    new_order_query = Order.objects.filter(pending=True)
                    for new in new_order_query:
                        new_order_list.append(new.table_number)
                    Order.objects.filter(pk=new_order_list[0]).update(pending=False)

            else:
                pass     
    
    for dish1 in ready_query:
        if dish1.starter_ready == True and dish1.mains_ready == True and dish1.deserts_ready == True and dish1.waiting_for_service==False :
            table_number = dish1.table_number
            Order.objects.filter(pk=table_number).update(waiting_for_service=True)
            waiting.append(dish1)
            return redirect(index)
            
            #return update_served(request)
            #return redirect(index)


    template = loader.get_template('order_taking/index.html')



    #new_order_list = []
    #if check:
    #new_order = Order.objects.filter(pending=True)
    #for item in new_order:
    #    if new_order_list.count() > 1:
    #        new_order_list.append(item.table_number)
    #table_number = new_order_list[0]
    #Order.objects.filter(pk=table_number).update(pending=False)


    query = Order.objects.filter(pending=False).order_by('table_number')
    for q in query:
        if q.waiting_for_service == False:
            order_list.append(q)
            #if q.served==False and q.waiting_for_service==True:
                #for serve in ready:
                    #if serve.served==False:
                #total_seconds = 3
                #while total_seconds > 0:
                #    timer = datetime.timedelta(seconds = total_seconds)
                #    print(timer, end="/r")
                #    time.sleep(1)
                #    total_seconds -= 1
                #return update_served(request) 
        #elif q.served==False and q.waiting_for_service==False:
        #    return redirect(index)

        
         
         

    #if Order.objects.filter(waiting_for_service=True) and Order.objects.filter(served=False):
    #    total_seconds = 3
    #    while total_seconds > 0:
    #        timer = datetime.timedelta(seconds = total_seconds)
    #        print(timer, end="/r")
    #        time.sleep(1)
    #        total_seconds -= 1
    #    return update_served(request)
    




    context = {
        'order_list': order_list,
        'waiting': waiting, 
    }
    
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

def update_served(request):
    ready_query = Order.objects.filter(pending=False)
    for dish1 in ready_query:
        if dish1.starter_ready == True and dish1.mains_ready == True and dish1.deserts_ready == True and dish1.waiting_for_service==True and dish1.served==False:
                table_number = dish1.table_number
                total_seconds = 3
                while total_seconds > 0:
                    timer = datetime.timedelta(seconds = total_seconds)
                    print(timer, end="/r")
                    time.sleep(1)
                    total_seconds -= 1
                    Order.objects.filter(pk=table_number).update(served=True)
    return redirect(index)
#    pending_update = Order.objects.filter(waiting_for_service=True)
#    update_list = []
#    table_number_list = []
#    total_seconds = 3
#    while total_seconds > 0:
#        timer = datetime.timedelta(seconds = total_seconds)
#        print(timer, end="/r")
#        time.sleep(1)
#        total_seconds -= 1
#    for item in pending_update:
#        if item.served == False:
#            update_list.append(item)
#        for entry in update_list:
#            table_number_list.append(entry.table_number)
#        for table_number in table_number_list:
#            response = Order.objects.filter(pk = table_number).update(served=True)
#            return redirect(index)


