# Generated by Django 2.1.1 on 2019-02-18 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('desc', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(blank=True, max_length=300, null=True)),
                ('photo', models.ImageField(upload_to='')),
                ('album_id', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='cover',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Album_Organizer.Photo'),
        ),
    ]
