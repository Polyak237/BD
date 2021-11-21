# Generated by Django 3.2.6 on 2021-11-08 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='pets',
        ),
        migrations.AddField(
            model_name='pet',
            name='client',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='pets', to='main_app.client', verbose_name='Client'),
            preserve_default=False,
        ),
    ]
