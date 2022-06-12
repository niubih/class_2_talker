# Generated by Django 2.2 on 2022-05-08 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('class_2_talker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='text',
            field=models.CharField(max_length=200),
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='class_2_talker.Topic')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]
