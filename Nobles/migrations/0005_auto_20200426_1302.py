# Generated by Django 2.1.7 on 2020-04-26 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Nobles', '0004_auto_20200423_2049'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homeworks',
            options={'ordering': ['added'], 'verbose_name_plural': 'Homeworks'},
        ),
        migrations.AlterModelOptions(
            name='notice',
            options={'ordering': ['last_updated'], 'verbose_name_plural': 'Notice'},
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['id']},
        ),
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='classroom',
        ),
    ]
