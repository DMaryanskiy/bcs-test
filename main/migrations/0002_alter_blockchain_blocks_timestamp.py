# Generated by Django 3.2.5 on 2021-07-19 09:13

from django.db import migrations
import unixtimestampfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blockchain_blocks',
            name='timestamp',
            field=unixtimestampfield.fields.UnixTimeStampField(default=0.0),
        ),
    ]