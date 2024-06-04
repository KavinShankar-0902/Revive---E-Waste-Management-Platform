# Generated by Django 5.0.3 on 2024-03-07 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EWasteCollection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waste_image', models.ImageField(upload_to='ewaste_images/')),
                ('waste_type', models.CharField(max_length=100)),
                ('quantity', models.PositiveIntegerField()),
                ('location', models.CharField(max_length=200)),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
