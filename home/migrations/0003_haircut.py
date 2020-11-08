# Generated by Django 3.1.2 on 2020-11-08 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Haircut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('type_id', models.CharField(max_length=50)),
                ('card_id', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('heading', models.CharField(max_length=100)),
                ('time', models.IntegerField()),
                ('desc', models.TextField()),
            ],
            options={
                'db_table': 'Haircut',
            },
        ),
    ]