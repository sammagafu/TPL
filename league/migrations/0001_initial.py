# Generated by Django 4.2.15 on 2024-10-21 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('division', models.CharField(blank=True, max_length=50, null=True)),
                ('season', models.CharField(max_length=9)),
                ('founded_year', models.IntegerField(blank=True, null=True)),
                ('number_of_teams', models.IntegerField(default=0)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='league_logos/')),
                ('website', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
