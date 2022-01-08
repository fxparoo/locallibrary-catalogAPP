# Generated by Django 3.2.10 on 2021-12-12 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_alter_language_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.ForeignKey(help_text='select a language for this book', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.language'),
        ),
    ]
