# Generated by Django 2.1.3 on 2018-11-24 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_change_entity_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Synonym',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.Entity')),
            ],
        ),
    ]
