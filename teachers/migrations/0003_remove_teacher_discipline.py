# Generated by Django 3.2.5 on 2021-08-02 15:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_teacher_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='discipline',
        ),
    ]