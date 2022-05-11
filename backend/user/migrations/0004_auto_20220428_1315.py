# Generated by Django 3.1.14 on 2022-04-28 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20220427_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='new_password',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Новый пароль'),
        ),
        migrations.AddField(
            model_name='user',
            name='restore_password_confirm_code_email',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Код сброса пароля по почте'),
        ),
        migrations.AddField(
            model_name='user',
            name='restore_password_confirm_code_phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Код сброса пароля по телефону'),
        ),
    ]
