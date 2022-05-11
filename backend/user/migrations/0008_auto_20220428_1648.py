# Generated by Django 3.1.14 on 2022-04-28 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20220428_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_code_send_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email_confirmation_code',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Код подтверждения email'),
        ),
    ]
