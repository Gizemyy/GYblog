# Generated by Django 3.1.7 on 2021-04-13 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20210412_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_auther', models.CharField(max_length=50, verbose_name='isim')),
                ('comment_content', models.CharField(max_length=200, verbose_name='yorum')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='article.article', verbose_name='makale')),
            ],
        ),
    ]
