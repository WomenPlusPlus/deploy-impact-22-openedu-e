# Generated by Django 4.1.3 on 2022-11-14 15:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0012_alter_resource_key_competence_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='key_competence',
            field=models.IntegerField(choices=[(1, 'Literacy'), (2, 'Multilingual'), (3, 'Mathematical, science, technology, engineering'), (4, 'Digital'), (5, 'Personal, social, learning to learn'), (6, 'Citizenship'), (7, 'Entrepreneurship'), (8, 'Cultural awareness and expression')]),
        ),
        migrations.AlterField(
            model_name='resource',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 14, 15, 59, 34, 717008, tzinfo=datetime.timezone.utc), verbose_name='date published'),
        ),
    ]
