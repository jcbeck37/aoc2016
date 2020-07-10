# Generated by Django 3.0.8 on 2020-07-10 20:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BalanceBot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('botId', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Coordinates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('xCoord', models.IntegerField()),
                ('yCoord', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Directions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rotation', models.CharField(max_length=1)),
                ('distance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Microchip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('botHolding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aoc2016.BalanceBot')),
            ],
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('outId', models.IntegerField()),
                ('chip1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aoc2016.Microchip')),
            ],
        ),
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.CharField(max_length=20)),
                ('num', models.IntegerField()),
                ('target', models.CharField(max_length=20)),
                ('keyBot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aoc2016.BalanceBot')),
            ],
        ),
    ]