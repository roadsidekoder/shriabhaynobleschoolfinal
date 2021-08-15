# Generated by Django 2.1.7 on 2021-08-15 11:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Nobles', '0002_auto_20201024_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='schoolClassroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classroom', models.CharField(max_length=100)),
                ('cid', models.IntegerField(null=True)),
                ('session', models.DateField(default=django.utils.timezone.now)),
                ('created', models.DateField(auto_now_add=True, null=True)),
                ('last_updated', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Classroom',
                'ordering': ['cid'],
            },
        ),
        migrations.RemoveField(
            model_name='toppers',
            name='student',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.AddField(
            model_name='schoolclassroom',
            name='toppers',
            field=models.ManyToManyField(to='Nobles.Toppers'),
        ),
    ]