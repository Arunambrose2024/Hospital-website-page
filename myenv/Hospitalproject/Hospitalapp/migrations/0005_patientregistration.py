# Generated by Django 5.0.4 on 2024-04-25 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospitalapp', '0004_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='patientregistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pname', models.CharField(max_length=250)),
                ('pemail', models.CharField(max_length=300)),
                ('pcontact', models.CharField(max_length=300)),
                ('gender', models.CharField(max_length=250)),
                ('paddress', models.CharField(max_length=350)),
                ('pdob', models.CharField(max_length=300)),
                ('username', models.CharField(max_length=400)),
                ('password', models.CharField(max_length=400)),
            ],
        ),
    ]