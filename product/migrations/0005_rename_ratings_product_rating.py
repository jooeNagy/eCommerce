# Generated by Django 5.1 on 2024-08-14 22:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_rename_rating_review_ratings_alter_review_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='ratings',
            new_name='rating',
        ),
    ]