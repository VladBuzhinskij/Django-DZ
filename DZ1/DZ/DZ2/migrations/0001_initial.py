# Generated by Django 5.0.3 on 2024-04-09 18:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Названее')),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True, verbose_name='URL')),
                ('discription', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Цена')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('date_create', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'db_table': 'Product',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Userss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Имя')),
                ('email', models.EmailField(max_length=150, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=150, unique=True, verbose_name='Телефон')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Адрес')),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True, verbose_name='URL')),
                ('date_create', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'db_table': 'Userss',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='Сумма заказа')),
                ('date_create', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DZ2.products', verbose_name='Товар')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DZ2.userss', verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
                'db_table': 'User',
                'ordering': ('id',),
            },
        ),
    ]
