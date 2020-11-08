# Generated by Django 3.1.2 on 2020-11-08 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=50)),
                ('service_heading', models.CharField(max_length=50)),
                ('service_desc', models.TextField()),
                ('service_icon', models.ImageField(upload_to='home/static/img/service_icons')),
                ('card_heading', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'services',
            },
        ),
    ]
