# Generated by Django 3.1.4 on 2020-12-28 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='number',
            field=models.DecimalField(decimal_places=1, default='Null', max_digits=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='upload',
            field=models.FileField(max_length=200, null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
