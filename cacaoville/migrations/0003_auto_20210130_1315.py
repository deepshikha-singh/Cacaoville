# Generated by Django 3.1.5 on 2021-01-30 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cacaoville', '0002_chocolate_flavor'),
    ]

    operations = [
        migrations.CreateModel(
            name='flavour',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('img', models.ImageField(blank='true', null='true', upload_to='Flavour')),
            ],
            options={
                'verbose_name': 'Flavour',
                'verbose_name_plural': 'Flavours',
            },
        ),
        migrations.RemoveField(
            model_name='chocolate',
            name='flavor',
        ),
        migrations.DeleteModel(
            name='flavor',
        ),
        migrations.AddField(
            model_name='chocolate',
            name='flavour',
            field=models.ManyToManyField(to='cacaoville.flavour', verbose_name='flavour'),
        ),
    ]
