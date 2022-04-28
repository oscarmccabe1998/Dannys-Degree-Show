from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Order, starter, table
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
import time
import datetime
import Board
import neopixel


def index(request):
    order_list = []
    waiting = []
    test = '0'
    ready = Order.objects.filter(waiting_for_service=True)
    for dish in ready:
        if dish.served==False:
            waiting.append(dish)
            if dish.waiting_for_service==True:
                print(waiting)
    
    ready_query = Order.objects.filter(pending=False)
    ready_query2 = Order.objects.filter(waiting_for_service=True)
    for dish2 in ready_query2:
        if dish2:

            if dish2.served==False:
                table_number = dish2.table_number
                Order.objects.filter(pk=table_number).update(served=True)

                check = Order.objects.filter(pending=True).count()
                new_order_list = []
                if check < 0:
                    pass
                if Order.objects.filter(pending=True):
                    new_order_query = Order.objects.filter(pending=True)
                    for new in new_order_query:
                        new_order_list.append(new.table_number)
                    Order.objects.filter(pk=new_order_list[0]).update(pending=False)
                    #return(update_served(request))
            else:
                pass  

            #if dish2.served == True:
            #    return(update_served(request))
    
    for dish1 in ready_query:
        if dish1.starter_ready == True and dish1.mains_ready == True and dish1.deserts_ready == True and dish1.waiting_for_service==False :
            table_number = dish1.table_number
            Order.objects.filter(pk=table_number).update(waiting_for_service=True)
            waiting.append(dish1)
            return redirect(index)
            



    template = loader.get_template('order_taking/index.html')





    query = Order.objects.filter(pending=False).order_by('table_number')
    for q in query:
        if q.waiting_for_service == False:
            order_list.append(q)




    context = {
        'order_list': order_list,
        'waiting': waiting, 
    }
    
    return render(request, 'order_taking/index.html', context)
    
def update_starter(request, table_number):
    pixel_pin = board.D18
    num_pixels = 84
    ORDER = neopixel.RGBW

    pixels = neopixel.NeoPixel(
        pixel_pin, num_pixels, brightness=2.0, auto_write=False, pixel_order=ORDER
    )
    starter = Order.objects.get(pk=table_number)
    response = Order.objects.filter(pk = table_number).update(starter_ready=True)
    if starter.table_number == 1:
        pixels[20] = ((0, 0, 0, 255))
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

    total_seconds = 300
    
    while total_seconds > 0:
        timer = datetime.timedelta(seconds = total_seconds)
        print(timer, end="/r")
        time.sleep(1)
        total_seconds -= 1
                    
    return redirect(index)

def LED_control(request):
    pixel_pin = board.D18
    num_pixels = 84
    ORDER = neopixel.RGBW

    pixels = neopixel.NeoPixel(
        pixel_pin, num_pixels, brightness=2.0, auto_write=False, pixel_order=ORDER
    )
    return redirect(index)