# Generated by Django 3.2.3 on 2021-05-29 16:19

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_portfolio_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='image',
            field=stdimage.models.StdImageField(blank=True, upload_to='static'),
        ),
    ]
