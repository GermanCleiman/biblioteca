# Generated by Django 2.0.6 on 2019-07-03 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0002_auto_20190703_1126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='autor_id',
        ),
        migrations.AddField(
            model_name='libro',
            name='autor_id',
            field=models.ManyToManyField(to='libro.Autor'),
        ),
    ]