# Generated by Django 4.0.2 on 2022-03-13 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_mytable_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytable',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]