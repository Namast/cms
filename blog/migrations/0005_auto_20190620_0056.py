# Generated by Django 2.2.2 on 2019-06-19 21:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20190620_0007'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Комментарий')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('moderation', models.BooleanField(default=False, verbose_name='Опубликовать')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('description', models.TextField(max_length=500, verbose_name='Превью статьи')),
                ('text', models.TextField(verbose_name='Статья')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('publish_data', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата публикации')),
                ('published', models.BooleanField(default=True, verbose_name='Опубликовать')),
                ('sort', models.PositiveIntegerField(default=0, unique=True, verbose_name='Порядок')),
                ('view', models.PositiveIntegerField(default=0, verbose_name='Просмотры')),
                ('slug', models.SlugField(max_length=150, verbose_name='url')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Category', verbose_name='Категория')),
                ('tags', models.ManyToManyField(to='blog.Tag', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AddField(
            model_name='commentpost',
            name='post',
            field=models.ForeignKey(on_delete=0, to='blog.Post'),
        ),
    ]
