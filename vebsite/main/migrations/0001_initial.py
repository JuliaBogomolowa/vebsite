# Generated by Django 4.1.3 on 2022-11-05 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Номер')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('task', models.TextField(verbose_name='Описание')),
                ('prim', models.CharField(max_length=50, verbose_name='Примечание')),
            ],
        ),
    ]
