# Generated by Django 3.2.9 on 2021-11-26 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_uploadfilemodel_exp_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadfilemodel',
            name='exp_time',
        ),
        migrations.CreateModel(
            name='ExpireTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp_time', models.DateTimeField(blank=True, null=True)),
                ('file', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.uploadfilemodel')),
            ],
        ),
    ]