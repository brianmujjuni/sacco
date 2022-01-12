# Generated by Django 4.0.1 on 2022-01-12 05:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transactionId', models.CharField(default='000-00-D', max_length=266, primary_key=True, serialize=False)),
                ('accountNo', models.CharField(max_length=266)),
                ('accountName', models.CharField(max_length=266)),
                ('accountType', models.CharField(max_length=50)),
                ('transanctionType', models.CharField(max_length=30)),
                ('transactionAmount', models.FloatField()),
                ('balanceAmount', models.FloatField()),
                ('transactionDate', models.DateTimeField(auto_now_add=True)),
                ('regBy', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-transactionDate',),
            },
        ),
    ]