# Generated by Django 4.2 on 2023-04-22 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fraud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('account_no', models.CharField(max_length=20)),
                ('amount', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
