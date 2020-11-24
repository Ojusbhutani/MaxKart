# Generated by Django 3.1.2 on 2020-11-23 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='pincode',
            field=models.CharField(default=125001, max_length=7),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='state',
            field=models.CharField(max_length=70),
        ),
    ]