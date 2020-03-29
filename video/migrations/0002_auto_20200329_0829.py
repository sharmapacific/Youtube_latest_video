# Generated by Django 2.2.1 on 2020-03-29 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(blank=True, max_length=1000, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created At')),
                ('exhaust_on', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='videoinfo',
            name='description',
            field=models.CharField(db_index=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='videoinfo',
            name='title',
            field=models.CharField(db_index=True, max_length=2000, null=True),
        ),
    ]