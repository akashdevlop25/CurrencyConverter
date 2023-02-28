# Generated by Django 4.1.7 on 2023-02-24 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('converter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='data',
            name='date',
        ),
        migrations.AlterField(
            model_name='data',
            name='amount',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='data',
            name='currency1',
            field=models.CharField(default='PLN', max_length=3),
        ),
        migrations.AlterField(
            model_name='data',
            name='currency2',
            field=models.CharField(default='EUR', max_length=3),
        ),
    ]
