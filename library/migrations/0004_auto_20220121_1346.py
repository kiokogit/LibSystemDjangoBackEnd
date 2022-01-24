# Generated by Django 3.2.7 on 2022-01-21 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_comments_forbook'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='forBook',
        ),
        migrations.AddField(
            model_name='books',
            name='comments',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.comments'),
        ),
        migrations.AlterField(
            model_name='books',
            name='RFIDtag',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='author',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='coverImage',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='books',
            name='discipline',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='noOfPages',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='subject',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='views',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
