# Generated by Django 2.2.26 on 2022-03-08 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TwosComplement', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='questionnaire',
            name='answer10',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionnaire',
            name='answer9',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
