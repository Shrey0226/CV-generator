# Generated by Django 5.0.2 on 2024-02-28 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.IntegerField(max_length=15)),
                ('adress', models.CharField(max_length=200)),
                ('Degree', models.CharField(max_length=200)),
                ('university', models.CharField(max_length=200)),
                ('duration', models.CharField(max_length=200)),
                ('summary', models.TextField(max_length=2000)),
                ('skills', models.TextField(max_length=500)),
                ('projects', models.TextField(max_length=2000)),
                ('work', models.TextField(max_length=2000)),
                ('achivement', models.TextField(max_length=2000)),
                ('links', models.TextField(max_length=2000)),
            ],
        ),
    ]
