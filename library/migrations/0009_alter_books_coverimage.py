# Generated by Django 3.2.7 on 2022-01-24 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_alter_borrowedbooks_finesaccumulated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='coverImage',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]