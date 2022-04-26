from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Order, starter, table
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect

def index(request):
    order_list = []
    waiting = []
    ready = Order.objects.filter(waiting_for_service=True)
    for dish in ready:
        waiting.append(dish)
    print(waiting)
    ready_query = Order.objects.filter(pending=False)
    for dish1 in ready_query:
        if dish1.starter_ready == True and dish1.mains_ready == True and dish1.deserts_ready == True and dish1.waiting_for_service==False :
            table_number = dish1.table_number
            Order.objects.filter(pk=table_number).update(waiting_for_service=True)
    

    template = loader.get_template('order_taking/index.html')
    check = Order.objects.filter(pending=False).count()
    if check < 6:
        Order.objects.filter
    print(check)
    query = Order.objects.filter(pending=False)
    for q in query:
        order_list.append(q)


    


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



