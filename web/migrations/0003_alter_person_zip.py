# Generated by Django 4.0.3 on 2022-04-02 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_person_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='zip',
            field=models.IntegerField(),
        ),
    ]
