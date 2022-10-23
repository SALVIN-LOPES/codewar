# Generated by Django 4.1.2 on 2022-10-22 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_event_preview'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-end_date']},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['avatar']},
        ),
        migrations.AlterField(
            model_name='submission',
            name='details',
            field=models.TextField(null=True),
        ),
    ]