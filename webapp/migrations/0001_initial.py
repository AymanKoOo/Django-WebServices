# Generated by Django 3.0 on 2020-05-01 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='picM',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('pic', models.BinaryField()),
            ],
        ),
    ]
