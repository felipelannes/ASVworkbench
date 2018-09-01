# Generated by Django 2.1 on 2018-08-25 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('physical_object', '0005_auto_20180825_0138'),
    ]

    operations = [
        migrations.CreateModel(
            name='PART',
            fields=[
                ('mass', models.DecimalField(decimal_places=3, help_text='in kg', max_digits=13, null=True, verbose_name='Mass')),
                ('lcg', models.DecimalField(decimal_places=3, help_text='in m', max_digits=6, null=True, verbose_name='LCG')),
                ('tcg', models.DecimalField(decimal_places=3, help_text='in m', max_digits=6, null=True, verbose_name='TCG')),
                ('vcg', models.DecimalField(decimal_places=3, help_text='in m', max_digits=6, null=True, verbose_name='VCG')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('part_name', models.CharField(max_length=32, verbose_name='Part Name')),
                ('group_system', models.PositiveSmallIntegerField(choices=[(100, 'Structure'), (200, 'Propulsion'), (300, 'Eletrical'), (400, 'Control'), (500, 'Auxiliary System'), (600, 'Outfit'), (700, 'Fixed Payload'), (800, 'Variable Payload')], verbose_name='Group System')),
                ('description', models.TextField(blank=True)),
                ('quantity', models.PositiveSmallIntegerField(verbose_name='Quantity')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
                'ordering': ['-mass'],
            },
        ),
        migrations.AddField(
            model_name='vessel',
            name='lcg',
            field=models.DecimalField(decimal_places=3, help_text='in m', max_digits=6, null=True, verbose_name='LCG'),
        ),
        migrations.AddField(
            model_name='vessel',
            name='mass',
            field=models.DecimalField(decimal_places=3, help_text='in kg', max_digits=13, null=True, verbose_name='Mass'),
        ),
        migrations.AddField(
            model_name='vessel',
            name='tcg',
            field=models.DecimalField(decimal_places=3, help_text='in m', max_digits=6, null=True, verbose_name='TCG'),
        ),
        migrations.AddField(
            model_name='vessel',
            name='vcg',
            field=models.DecimalField(decimal_places=3, help_text='in m', max_digits=6, null=True, verbose_name='VCG'),
        ),
        migrations.AddField(
            model_name='part',
            name='vessel_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='physical_object.VESSEL'),
        ),
    ]