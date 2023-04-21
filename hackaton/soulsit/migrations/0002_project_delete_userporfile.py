# Generated by Django 4.2 on 2023-04-21 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soulsit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=30)),
                ('project_budget', models.CharField(max_length=30)),
                ('project_category', models.CharField(max_length=254)),
                ('project_owner', models.CharField(max_length=100)),
                ('project_foto', models.CharField(max_length=100)),
                ('project_users', models.CharField(max_length=100)),
                ('project_creation_date', models.CharField(max_length=100)),
                ('project_details', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='UserPorfile',
        ),
    ]
