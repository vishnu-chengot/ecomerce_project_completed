# Generated by Django 4.1.1 on 2023-01-03 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('phone', models.BigIntegerField()),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
    ]
