# Generated by Django 2.0.3 on 2018-06-18 22:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('zhihu', '0003_auto_20180616_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='answercomment',
            name='add_time',
            field=models.DateTimeField(auto_now_add=True,
                                       default=django.utils.timezone.now,
                                       verbose_name='添加时间'),
            preserve_default=False,
        ),
    ]