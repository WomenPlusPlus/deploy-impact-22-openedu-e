# Generated by Django 4.1.3 on 2022-11-14 15:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0011_alter_resource_pub_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='key_competence',
            field=models.CharField(choices=[(1, 'Literacy'), (2, 'Multilingual'), (3, 'Mathematical, science, technology, engineering'), (4, 'Digital'), (5, 'Personal, social, learning to learn'), (6, 'Citizenship'), (7, 'Entrepreneurship'), (8, 'Cultural awareness and expression')], max_length=2),
        ),
        migrations.AlterField(
            model_name='resource',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 14, 15, 56, 39, 868686, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
    ]