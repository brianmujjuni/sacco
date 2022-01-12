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
            name='Account_Types',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branchName', models.CharField(max_length=50)),
                ('accountType', models.CharField(max_length=266)),
                ('description', models.TextField(blank=True)),
                ('currencyCode', models.CharField(max_length=20)),
                ('minimumBalance', models.FloatField()),
                ('withdrawCharge', models.IntegerField(default=0)),
                ('accountStatus', models.BooleanField(default=False)),
                ('regDate', models.DateTimeField(auto_now=True)),
                ('regBy', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Account Types',
            },
        ),
    ]