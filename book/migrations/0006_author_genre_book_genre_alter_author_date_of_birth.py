# Generated by Django 4.2.4 on 2023-09-04 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_remove_author_genre_remove_author_genre_de_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='genre',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='book.genre'),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='book.genre'),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]