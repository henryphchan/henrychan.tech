# Generated by Django 5.1.3 on 2025-02-02 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('supplier_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('ProductID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=200)),
                ('Description', models.TextField(blank=True, null=True)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('StockQuantity', models.PositiveIntegerField()),
                ('Suppliers', models.ManyToManyField(related_name='products', to='supplier_app.supplier')),
            ],
        ),
    ]
