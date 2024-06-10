# Generated by Django 5.0.6 on 2024-06-10 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('pages', models.IntegerField()),
                ('price', models.IntegerField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]