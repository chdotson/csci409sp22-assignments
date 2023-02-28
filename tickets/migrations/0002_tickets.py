# Generated by Django 4.1.5 on 2023-02-13 01:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat', models.CharField(max_length=10)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ticket_class', models.CharField(choices=[('F', 'First Class'), ('B', 'Business Class'), ('M', 'Main Cabin')], default='M', max_length=1)),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tickets.reservation')),
            ],
        ),
    ]
