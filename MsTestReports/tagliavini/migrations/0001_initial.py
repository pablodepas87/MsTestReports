# Generated by Django 3.0.7 on 2020-06-26 10:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TagliaviniReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tester_name', models.CharField(max_length=30)),
                ('tester_surname', models.CharField(max_length=30)),
                ('board_serial', models.CharField(max_length=6)),
                ('dt_start_test', models.DateTimeField(verbose_name='start_test')),
                ('touchscreen', models.BooleanField()),
                ('brightness', models.BooleanField()),
                ('buzzer', models.BooleanField()),
                ('usb', models.BooleanField()),
                ('serial_work', models.BooleanField()),
                ('dt_end_test', models.DateTimeField(verbose_name='end_test')),
                ('sw_version', models.CharField(max_length=10)),
                ('owner', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tagliavini_report', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]