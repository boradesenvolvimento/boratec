# Generated by Django 4.1.7 on 2023-03-14 20:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adm_tools', '0003_alter_purchaserequest_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaserequest',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 14, 17, 41, 2, 215376)),
        ),
    ]
