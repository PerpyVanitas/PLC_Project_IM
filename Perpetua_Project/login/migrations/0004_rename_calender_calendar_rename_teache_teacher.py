# Generated by Django 5.1.2 on 2024-11-03 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_holiday_slot_attendance_periods_alter_attendance_id_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Calender',
            new_name='Calendar',
        ),
        migrations.RenameModel(
            old_name='Teache',
            new_name='Teacher',
        ),
    ]
