# Generated by Django 4.0.4 on 2022-06-07 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_note_id_note_tid'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='monospace',
            field=models.BooleanField(default=False),
        ),
    ]
