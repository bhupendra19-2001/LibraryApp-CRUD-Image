# Generated by Django 4.2.2 on 2024-03-21 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_alter_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='describe',
            field=models.TextField(),
        ),
    ]
