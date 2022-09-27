# Generated by Django 4.1.1 on 2022-09-27 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('location', models.CharField(blank=True, max_length=500)),
            ],
            options={
                'db_table': 'my_log',
            },
        ),
    ]
