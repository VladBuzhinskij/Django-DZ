# Generated by Django 5.0.3 on 2024-04-12 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DZ2', '0003_alter_orders_options_alter_userss_date_create'),
    ]

    operations = [
        migrations.AddField(
            model_name='userss',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='userss', verbose_name='фото профиля'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='date_create',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='userss',
            name='date_create',
            field=models.DateField(auto_now_add=True),
        ),
    ]