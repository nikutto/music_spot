# Generated by Django 3.0.6 on 2020-05-06 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_spot', '0005_auto_20200506_0440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='date',
        ),
        migrations.RemoveField(
            model_name='song',
            name='youtube_embedded_link',
        ),
        migrations.RemoveField(
            model_name='song',
            name='youtube_link',
        ),
        migrations.AddField(
            model_name='song',
            name='youtube_video_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
