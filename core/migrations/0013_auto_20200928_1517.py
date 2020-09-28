# Generated by Django 2.2 on 2020-09-28 15:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_wallet_daily_login_fee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wallet',
            old_name='daily_login_fee',
            new_name='wallet_fee',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='facebook_share_fee',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='referral_fee',
        ),
        migrations.RemoveField(
            model_name='wallet',
            name='signup_fee',
        ),
        migrations.AddField(
            model_name='wallet',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wallet',
            name='wallet_id',
            field=models.CharField(default='00', max_length=25, unique=True),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]