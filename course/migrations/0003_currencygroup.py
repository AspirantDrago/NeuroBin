# Generated by Django 2.0.2 on 2018-02-26 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20180226_0905'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Наименование', max_length=16, null=True)),
            ],
        ),
    ]
