# Generated by Django 3.2.4 on 2024-06-03 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiRequestCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('api_category', models.CharField(max_length=255, verbose_name='API类别')),
                ('api_name', models.CharField(max_length=255, verbose_name='API名称')),
                ('request_count', models.IntegerField(default=0, verbose_name='请求次数')),
            ],
            options={
                'verbose_name': 'API请求次数',
                'verbose_name_plural': 'API请求次数',
                'unique_together': {('api_category', 'api_name')},
            },
        ),
    ]
