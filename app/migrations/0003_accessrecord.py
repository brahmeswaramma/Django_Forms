# Generated by Django 5.0.1 on 2024-01-07 10:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_webpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('author', models.CharField(max_length=100)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.webpage')),
            ],
        ),
    ]
