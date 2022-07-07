# Generated by Django 4.0.5 on 2022-06-26 23:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('perfil', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='dirigente',
            field=models.CharField(db_column='DIRIGENTE', max_length=50),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='telefone',
            field=models.CharField(db_column='TELEFONE', max_length=11),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]