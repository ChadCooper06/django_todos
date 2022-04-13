# Generated by Django 4.0.4 on 2022-04-13 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='label',
            field=models.CharField(default='Tasks', max_length=200),
        ),
        migrations.AlterField(
            model_name='todo',
            name='category',
            field=models.ManyToManyField(blank=True, to='todo_list.categories'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(auto_now_add=True, verbose_name='Date created'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
