# Generated by Django 3.2.6 on 2021-11-08 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('type', models.CharField(choices=[('Cat', 'Cat'), ('Dog', 'Dog')], default='Cat', max_length=3, verbose_name='Type')),
                ('weight', models.FloatField(verbose_name='Weight')),
                ('breed', models.CharField(max_length=50, verbose_name='Breed')),
                ('recommendations', models.TextField(blank=True, max_length=1000, verbose_name='Recommendations')),
            ],
            options={
                'verbose_name': 'Pet',
                'verbose_name_plural': 'Pets',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='First name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last name')),
                ('middle_name', models.CharField(blank=True, max_length=50, verbose_name='Middle name')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Phone number')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('pets', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='client', to='main_app.pet', verbose_name='Pets')),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
    ]
