# Generated by Django 3.0.4 on 2020-04-07 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RankModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=30)),
                ('score', models.IntegerField()),
                ('rank', models.IntegerField()),
            ],
        ),
    ]
