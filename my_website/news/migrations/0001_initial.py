# Generated by Django 4.1.6 on 2023-02-09 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Topic name')),
                ('anons', models.CharField(max_length=300, verbose_name='Announcement')),
                ('title_text', models.TextField(verbose_name='Article')),
                ('date', models.DateTimeField(verbose_name='Publication time')),
            ],
        ),
    ]