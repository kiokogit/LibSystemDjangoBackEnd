# Generated by Django 3.2.7 on 2022-01-21 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_auto_20220121_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books',
            name='comments',
        ),
        migrations.AddField(
            model_name='comments',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='library.books'),
        ),
    ]