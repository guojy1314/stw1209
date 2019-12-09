# Generated by Django 2.0.3 on 2018-06-30 21:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('zhihu', '0012_auto_20180629_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='image',
            field=models.ImageField(blank=True,
                                    default='image/default_topic.jpg',
                                    null=True, upload_to='image/%Y/%m/',
                                    verbose_name='话题图片'),
        ),
    ]