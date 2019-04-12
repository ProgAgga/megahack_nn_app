# Generated by Django 2.2 on 2019-04-12 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boilerplate', '0004_auto_20190412_2211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('port', models.IntegerField()),
                ('host', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('SQL', 'SQL'), ('REDIS', 'Redis'), ('HTTP', 'HTTP')], max_length=10)),
            ],
        ),
    ]
