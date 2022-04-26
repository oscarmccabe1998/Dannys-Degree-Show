# Generated by Django 4.0.4 on 2022-04-25 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_taking', '0013_order_pending'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='id',
        ),
        migrations.AlterField(
            model_name='order',
            name='table_number',
            field=models.IntegerField(choices=[(1, 'Table1'), (2, 'Table2'), (3, 'Table3'), (4, 'Table4'), (5, 'Table5'), (6, 'Table6'), (7, 'Table7'), (8, 'Table8'), (9, 'Table9'), (10, 'Table10'), (11, 'Table11'), (12, 'Table12'), (13, 'Table13'), (14, 'Table14'), (15, 'Table15'), (16, 'Table16')], default='1', primary_key=True, serialize=False),
        ),
    ]