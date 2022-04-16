from django.http import HttpResponse
from django.template import loader
from .models import Order

def index(request):
    order_list = Order.objects.all()       #passing data so it can be displayed within HTML
    template = loader.get_template('order_taking/index.html')
    context = {
        'order_list': order_list
    }
    return HttpResponse(template.render(context, request))

def detail(request, order_id):
    return HttpResponse("You are looking at Order %S." % order_id)

