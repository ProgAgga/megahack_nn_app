# Generated by Django 2.2 on 2019-04-12 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('boilerplate', '0004_auto_20190412_2211'),
    ]

    operations = [
        migrations.AddField(
            model_name='offerorder',
            name='client',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='boilerplate.Client'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offerorder',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='offerorder',
            name='date_processed',
            field=models.DateTimeField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='offerorder',
            name='dealer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='boilerplate.Dealer'),
        ),
        migrations.AddField(
            model_name='offerorder',
            name='id_hash',
            field=models.BinaryField(default=b'', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='offerorder',
            name='offer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='boilerplate.Offer'),
            preserve_default=False,
        ),
    ]
