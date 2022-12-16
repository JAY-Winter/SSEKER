# Generated by Django 3.2.13 on 2022-12-14 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20221214_0539'),
        ('accounts', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.ManyToManyField(blank=True, to='projects.Location'),
        ),
        migrations.AlterField(
            model_name='user',
            name='skill',
            field=models.ManyToManyField(blank=True, to='projects.Skill'),
        ),
    ]
