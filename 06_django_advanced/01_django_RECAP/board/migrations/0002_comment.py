# Generated by Django 2.2.6 on 2019-10-10 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=200)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='board.Article')),
            ],
        ),
    ]
