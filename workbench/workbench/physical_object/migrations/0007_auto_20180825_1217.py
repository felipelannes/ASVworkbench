# Generated by Django 2.1 on 2018-08-25 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('physical_object', '0006_auto_20180825_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='part',
            name='ixx',
            field=models.DecimalField(decimal_places=3, help_text='in kg·m²', max_digits=12, null=True, verbose_name='Ixx'),
        ),
        migrations.AddField(
            model_name='part',
            name='iyy',
            field=models.DecimalField(decimal_places=3, help_text='in kg·m²', max_digits=12, null=True, verbose_name='Iyy'),
        ),
        migrations.AddField(
            model_name='part',
            name='izz',
            field=models.DecimalField(decimal_places=3, help_text='in kg·m²', max_digits=12, null=True, verbose_name='Izz'),
        ),
        migrations.AddField(
            model_name='vessel',
            name='ixx',
            field=models.DecimalField(decimal_places=3, help_text='in kg·m²', max_digits=12, null=True, verbose_name='Ixx'),
        ),
        migrations.AddField(
            model_name='vessel',
            name='iyy',
            field=models.DecimalField(decimal_places=3, help_text='in kg·m²', max_digits=12, null=True, verbose_name='Iyy'),
        ),
        migrations.AddField(
            model_name='vessel',
            name='izz',
            field=models.DecimalField(decimal_places=3, help_text='in kg·m²', max_digits=12, null=True, verbose_name='Izz'),
        ),
    ]
