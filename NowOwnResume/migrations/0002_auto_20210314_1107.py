# Generated by Django 3.1.7 on 2021-03-14 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NowOwnResume', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suggesstions',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]