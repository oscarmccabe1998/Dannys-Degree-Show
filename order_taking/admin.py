from django.contrib import admin

from.models import Order, table, starter, main, desert, check

# Register your models here.


admin.site.register(Order)  #allows you to create orders through the admin section
admin.site.register(table)
admin.site.register(starter)
admin.site.register(main)
admin.site.register(desert)
admin.site.register(check)


