# Generated by Django 3.1.3 on 2021-02-12 15:14

from django.db import migrations, models
import posts.models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210212_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content_image',
            field=models.ImageField(blank=True, null=True, upload_to=posts.models.PathAndRename('uploads')),
        ),
        migrations.AlterField(
            model_name='post',
            name='front_image',
            field=models.ImageField(blank=True, null=True, upload_to=posts.models.PathAndRename('uploads')),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('post', models.ManyToManyField(to='posts.Post')),
            ],
        ),
    ]
