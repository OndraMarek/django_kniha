# Generated by Django 3.2 on 2021-05-03 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kniha', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zanry',
            name='zanr',
            field=models.CharField(help_text='Zadejte text o maximální délce 50 znaků; text musí být jedinečný', max_length=50, unique=True, verbose_name='Označení druhu zboží'),
        ),
    ]
