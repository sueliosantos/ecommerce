# Generated by Django 2.1.5 on 2019-01-24 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0002_order_orderitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_option',
            field=models.CharField(choices=[('deposit', 'Depósito'), ('pagseguro', 'PagSeguro'), ('paypal', 'Paypal')], default='deposit', max_length=20, verbose_name='Opção de Pagamento'),
        ),
    ]
