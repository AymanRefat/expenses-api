# Generated by Django 5.1.1 on 2024-09-15 08:23

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Groceries', 'Groceries'), ('Leisure', 'Leisure'), ('Electronics', 'Electronics'), ('Utilities', 'Utilities'), ('Clothing', 'Clothing'), ('Health', 'Health'), ('Others', 'Others')], max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
            ],
        ),
    ]
