# Generated by Django 3.2.5 on 2021-08-29 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('strating_price', models.IntegerField(null=True)),
                ('current_bid', models.IntegerField(null=True)),
                ('seller', models.CharField(default='Default_Value', max_length=64)),
                ('category', models.CharField(max_length=64)),
                ('image_link', models.CharField(blank=True, default=None, max_length=200, null=True)),
                ('winner', models.CharField(default='Default_value', max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Watchlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=64)),
                ('listing_id', models.IntegerField()),
            ],
        ),
    ]
