# Generated by Django 3.2.25 on 2024-04-28 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'verbose_name': 'Заказы', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterField(
            model_name='orders',
            name='comments',
            field=models.TextField(max_length='60', verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='name',
            field=models.TextField(blank=True, max_length='15', verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='tel',
            field=models.CharField(blank=True, max_length=12, verbose_name='Телефон'),
        ),
    ]
