# Generated by Django 3.2.8 on 2021-11-22 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20211108_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentitem',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]