# Generated by Django 3.0.6 on 2020-07-08 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('link', models.CharField(max_length=300)),
                ('views', models.CharField(max_length=50)),
            ],
        ),
    ]
