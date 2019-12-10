# Generated by Django 2.1.1 on 2019-02-28 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0005_auto_20190228_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='dates',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='freq',
            field=models.CharField(choices=[('One time', 'One time'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')], max_length=50),
        ),
    ]
