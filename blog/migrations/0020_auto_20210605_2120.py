# Generated by Django 3.2.4 on 2021-06-05 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20210605_1610'),
    ]

    operations = [
        migrations.RenameField(
            model_name='logoart',
            old_name='logo_name',
            new_name='project_name',
        ),
        migrations.RenameField(
            model_name='myart',
            old_name='myart_name',
            new_name='project_name',
        ),
        migrations.RenameField(
            model_name='videoart',
            old_name='video_name',
            new_name='project_name',
        ),
        migrations.RenameField(
            model_name='webdesign',
            old_name='design_name',
            new_name='project_name',
        ),
    ]