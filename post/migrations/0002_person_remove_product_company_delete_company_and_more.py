# Generated by Django 4.0.1 on 2022-03-23 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='company',
        ),
        migrations.DeleteModel(
            name='Company',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
