# Generated by Django 3.0 on 2021-02-23 02:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comentario_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comentario',
            old_name='id_post',
            new_name='post',
        ),
    ]