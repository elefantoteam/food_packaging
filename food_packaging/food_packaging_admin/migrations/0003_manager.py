# Generated by Django 4.1.3 on 2022-11-11 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_packaging_admin', '0002_formblockadminmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('managers_name', models.CharField(max_length=100, verbose_name='Имя менеджера')),
                ('managers_email', models.CharField(max_length=100, verbose_name='Емэйл для отправки почты')),
            ],
            options={
                'verbose_name': 'Менеджер',
                'verbose_name_plural': 'Менеджеры',
            },
        ),
    ]