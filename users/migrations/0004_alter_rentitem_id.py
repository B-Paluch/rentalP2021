# Generated by Django 3.2.8 on 2021-11-07 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20211107_2102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentitem',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
