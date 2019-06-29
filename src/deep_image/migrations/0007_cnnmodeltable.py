# Generated by Django 2.1.9 on 2019-06-29 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deep_image', '0006_auto_20190627_0623'),
    ]

    operations = [
        migrations.CreateModel(
            name='CnnModelTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('Top1Accuracy', models.CharField(max_length=10)),
                ('Top5Accuracy', models.CharField(max_length=10)),
                ('Parameters', models.CharField(max_length=20)),
                ('Depth', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name_plural': 'CNN MODELS',
            },
        ),
    ]