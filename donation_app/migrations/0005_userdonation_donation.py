# Generated by Django 4.1 on 2022-10-30 06:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_donation_money_needed'),
        ('donation_app', '0004_alter_userdonation_amount_of_donation'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdonation',
            name='donation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.donation'),
        ),
    ]