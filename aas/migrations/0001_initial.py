# Generated by Django 2.1.5 on 2019-01-05 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aasItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('quantity', models.PositiveSmallIntegerField()),
                ('checked', models.BooleanField(default=False)),
            ],
        ),
    ]