# Generated by Django 4.2 on 2023-04-27 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('previous_date', models.DateField()),
                ('cycle_length', models.PositiveIntegerField()),
                ('next_occurrence', models.DateField()),
                ('next_12_occurrences', models.TextField()),
                ('ovulation_date', models.DateField()),
                ('flow_date', models.DateField()),
                ('safe_periods', models.TextField()),
                ('fertile_periods', models.TextField()),
            ],
        ),
    ]
