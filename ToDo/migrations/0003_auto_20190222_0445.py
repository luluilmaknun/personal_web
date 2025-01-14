# Generated by Django 2.1.1 on 2019-02-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0002_event_dates'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('color', models.CharField(choices=[('Black', 'Black'), ('Red', 'Red'), ('Blue', 'Blue')], max_length=10)),
            ],
        ),
        migrations.AlterField(
            model_name='event',
            name='freq',
            field=models.CharField(choices=[('One time', 'One time'), ('Weekly', 'Weekly'), ('Monthly', 'Monthly')], max_length=50),
        ),
    ]
