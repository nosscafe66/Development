# Generated by Django 3.2.3 on 2021-05-16 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='create',
            name='key',
            field=models.IntegerField(),
        ),
    ]