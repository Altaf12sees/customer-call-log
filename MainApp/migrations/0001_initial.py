# Generated by Django 4.0 on 2021-12-10 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallLogsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_idno', models.CharField(max_length=10)),
                ('serial_no', models.CharField(max_length=50)),
                ('mobile_no', models.CharField(max_length=20)),
                ('call_reason', models.CharField(choices=[('Information', 'Information'), ('Inquiries', 'Inquiries'), ('Complaints', 'Complaints'), ('Support', 'Support')], default='', max_length=200)),
                ('remark', models.CharField(max_length=100)),
                ('items', models.CharField(max_length=255)),
                ('call_action', models.CharField(choices=[('Answered', 'Answered'), ('Rejected', 'Rejected')], default='', max_length=100)),
                ('approval', models.CharField(choices=[('Initial', 'Initial'), ('Pending', 'Pending'), ('Approved', 'Approved')], default='', max_length=10)),
                ('call_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.CharField(default=476566, max_length=50)),
                ('product_name', models.CharField(max_length=100)),
                ('product_type', models.CharField(max_length=100)),
                ('customer_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('mobile_no', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='UsersModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('SuperAdmin', 'SuperAdmin'), ('Admin', 'Admin'), ('Agent', 'Agent')], default='Admin', max_length=50)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
