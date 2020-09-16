# Generated by Django 2.0.8 on 2020-09-16 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0010_auto_20200915_2108'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signup_fee', models.FloatField(default='400')),
                ('referral_fee', models.FloatField(default='0')),
                ('facebook_share_fee', models.FloatField(default='0')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='referral',
            name='user',
        ),
        migrations.DeleteModel(
            name='Referral',
        ),
    ]