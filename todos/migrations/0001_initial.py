# Generated by Django 5.0.5 on 2024-05-16 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField()),
                ('finished_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
