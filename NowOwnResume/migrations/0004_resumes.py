# Generated by Django 3.1.7 on 2021-03-14 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NowOwnResume', '0003_auto_20210314_1108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resumes',
            fields=[
                ('resume_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='NILL', max_length=40)),
                ('address', models.CharField(default='NILL', max_length=450)),
                ('mob', models.CharField(default='none', max_length=20)),
            ],
        ),
    ]
