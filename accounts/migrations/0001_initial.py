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
            name='individual_standin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountNo', models.CharField(default='MZ-000-D', max_length=266, unique=True)),
                ('accountName', models.CharField(max_length=266)),
                ('firstName', models.CharField(max_length=266)),
                ('lastName', models.CharField(max_length=266)),
                ('gender', models.CharField(default='Male', max_length=10)),
                ('dob', models.DateField()),
                ('ninNumber', models.CharField(max_length=266)),
                ('contact', models.CharField(default='000,0000', max_length=20)),
                ('email', models.EmailField(default='example@gmail.com', max_length=254)),
                ('regDate', models.DateTimeField(auto_now=True)),
                ('regBy', models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Individual Account Standins',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('accountNo', models.CharField(max_length=266, primary_key=True, serialize=False)),
                ('accountType', models.CharField(max_length=266)),
                ('currency', models.CharField(max_length=10)),
                ('accountName', models.CharField(max_length=266)),
                ('firstName', models.CharField(max_length=266)),
                ('lastName', models.CharField(max_length=266)),
                ('otherName', models.CharField(blank=True, max_length=266)),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('nationality', models.CharField(max_length=266)),
                ('religion', models.CharField(max_length=20)),
                ('ninNumber', models.CharField(blank=True, max_length=266)),
                ('ninImage', models.ImageField(upload_to='nin_images/%Y/%m/%d/')),
                ('phoneNo1', models.CharField(max_length=20)),
                ('phoneNo2', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('occupation', models.CharField(max_length=100)),
                ('companyName', models.CharField(max_length=266)),
                ('nextOfKinName', models.CharField(max_length=266)),
                ('relationship', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=20)),
                ('profilePic', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('openingFees', models.FloatField()),
                ('accountStatus', models.CharField(default='Pending', max_length=20)),
                ('regDate', models.DateField()),
                ('date1', models.DateTimeField(auto_now_add=True)),
                ('regBy', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Individual Accounts',
            },
        ),
    ]