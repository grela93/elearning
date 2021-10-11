# Generated by Django 3.2.6 on 2021-10-03 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_auto_20211003_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='difficulity',
            field=models.CharField(choices=[('Dễ', 'Dễ'), ('Trung bình', 'Trung bình'), ('Khó', 'Khó')], max_length=10),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='show_result',
            field=models.CharField(choices=[('Không', 'Không'), ('Có', 'Có')], default='Có', max_length=10),
        ),
    ]
