# Generated by Django 5.0.4 on 2024-05-23 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospitalapp', '0009_rename_appoinment_appointment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctorregistration',
            old_name='spln',
            new_name='Dname',
        ),
        migrations.AddField(
            model_name='doctorregistration',
            name='docnum',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
