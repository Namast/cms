# Generated by Django 2.2.2 on 2019-07-14 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='template',
            field=models.CharField(default='blog/post_list.html', max_length=500, verbose_name='Шаблон'),
        ),
    ]