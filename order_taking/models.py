from django.db import models
import datetime
from django.utils import timezone

#admin oscarm pwd dannysdegreeshow

class Order(models.Model):  #class to pass data to database 
    class TableChoice(models.IntegerChoices):   #defining tables for the orders 
        Table1 = 1
        Table2 = 2
        Table3 = 3
        Table4 = 4
        Table5 = 5
        Table6 = 6
        Table7 = 7
        Table8 = 8
        Table9 = 9
        Table10 = 10
        Table11 = 11
        Table12 = 12
        Table13 = 13
        Table14 = 14
        Table15 = 15
        Table16 = 16

    
    Date = models.DateTimeField(default=datetime.datetime.now)      #all feilds that will be in the database table
    ref = models.CharField(max_length=200, blank=True)
    table_number = models.IntegerField(choices=TableChoice.choices, default='1', primary_key=True)
    starters = models.CharField(max_length=300)
    starter_ready = models.BooleanField(default=False)
    mains = models.CharField(max_length=300)
    mains_ready = models.BooleanField(default=False)
    deserts = models.CharField(max_length=300)
    deserts_ready = models.BooleanField(default=False)
    waiting_for_service = models.BooleanField(default=False)
    pending = models.BooleanField(default=False)
    served = models.BooleanField(default=False)

    def __str__(self):
        return self.mains
        return self.deserts
        return self.starters

class table(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    class TableChoice(models.IntegerChoices):   #defining tables for the orders 
        Table1 = 1
        Table2 = 2
        Table3 = 3
        Table4 = 4
        Table5 = 5
        Table6 = 6
        Table7 = 7
        Table8 = 8
        Table9 = 9
        Table10 = 10
        Table11 = 11
        Table12 = 12
        Table13 = 13
        Table14 = 14
        Table15 = 15
        Table16 = 16
    table_number = models.IntegerField(choices=TableChoice.choices, default='1')
    Date = models.DateTimeField(default=datetime.datetime.now)
    ref = models.CharField(max_length=200, blank=True)

class starter(models.Model):
    STARTER = (
        ('Soup of the day', 'Soup of the day'),     #Menu options to make data entry on the back end easier 
        ('Roasted red pepper hummus', 'Roasted red pepper hummus'),
        ('Charcuterie Board', 'Charcuterie Board'),
        ('Arbroath Smokie Risotto', 'Arbroath Smokie Risotto'),
        ('Hot Wings', 'Hot Wings'),
        ('Duck Leg & Fig Terrine', 'Duck Leg & Fig Terrine'),
        ('Beet Root Salad', 'Beet Root Salad'),
    )
    table_number = models.ForeignKey(table, on_delete=models.CASCADE)
    starters = models.CharField(max_length=25, choices=STARTER)

class main(models.Model):
    MAIN = (
        ('Ribeye Steak', 'Ribeye Steak'),
        ('Sirloin Steak', 'Sirloin Steak'),
        ('Cheese Burger', 'Cheese Burger'),
        ('Black And Blue Burger', 'Black And Blue Burger'),
        ('Moving Mountain', 'Moving Mountain'),
        ('The Baxter', 'The Baxter'),
        ('Miss Daisy', 'Miss Daisy'),
        ('Beer Battered, Haddock', 'Beer Battered, Haddock'),
        ('Cod Fillet', 'Cod Fillet'),
        ('Perthshire Duck Breast', 'Perthshire Duck Breast'),
        ('Burgundy Beef', 'Burgundy Beef'),
        ('Mushroom & Tarragon Linguine', 'Mushroom & Tarragon Linguine'),
        ('Spiced Polenta', 'Spiced Polenta'),
        ('Mac and Cheese', 'Mac and Cheese'),

    )
    table_number = models.ForeignKey(table, on_delete=models.CASCADE)
    mains = models.CharField(max_length=28, choices=MAIN)

class desert(models.Model):
    DESERT = (
        ('Bread & Butter Pudding', 'Bread & Butter Pudding'),
        ('Praline Chocolate Tart', 'Praline Chocolate Tart'),
        ('Lavender Panna Cotta', 'Lavender Panna Cotta'),
        ('Sticky Toffee Sundae', 'Sticky Toffee Sundae'),
        ('Clarckies Ice Cream', 'Clarckies Ice Cream'),
        ('Cheese Board', 'Cheese Board'),
    )
    table_number = models.ForeignKey(table, on_delete=models.CASCADE)
    deserts = models.CharField(max_length=22, choices=DESERT)

class check(models.Model):
    table_number =  models.ForeignKey(table, on_delete=models.CASCADE)
    starter =  models.ForeignKey(starter, on_delete=models.CASCADE)
    main = models.ForeignKey(main, on_delete=models.CASCADE)
    desert = models.ForeignKey(desert, on_delete=models.CASCADE)
