# Generated by Django 4.0.4 on 2022-04-25 23:56

import django.core.validators
from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('nome_instituicao', models.CharField(db_column='NOME_INSTITUICAO', max_length=50)),
                ('dirigente', models.CharField(db_column='DIRIGENTE', max_length=20)),
                ('logradouro', models.CharField(db_column='LOGRADOURO', max_length=50)),
                ('numero', models.CharField(db_column='NUMERO', max_length=5, validators=[django.core.validators.MinLengthValidator(1), django.core.validators.MaxLengthValidator(5)])),
                ('bairro', models.CharField(db_column='BAIRRO', max_length=25)),
                ('cidade', models.CharField(db_column='CIDADE', max_length=30)),
                ('UF', models.CharField(db_column='UF', max_length=2)),
                ('telefone', models.CharField(db_column='TELEFONE', max_length=10)),
                ('fax', models.CharField(db_column='FAX', max_length=10)),
                ('site', models.CharField(db_column='SITE', max_length=50)),
                ('email_instituicao', models.CharField(db_column='EMAIL_INSTITUICAO', max_length=50)),
            ],
            options={
                'verbose_name': 'perfil',
                'verbose_name_plural': 'perfis',
                'db_table': 'PERFIL',
            },
        ),
    ]
