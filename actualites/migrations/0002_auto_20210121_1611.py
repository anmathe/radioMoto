# Generated by Django 3.1.4 on 2021-01-21 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actualites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AproposdeNous_laRadio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titreduMessage', models.CharField(max_length=200, null=True)),
                ('message_aux_auditeurs', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AproposdeNous_NotreEquipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomdelEquipe', models.CharField(max_length=100, null=True)),
                ('texteEquipe', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AproposdeNous_ProjetdAvenir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titreduProjet', models.CharField(max_length=200)),
                ('objectifsProjet', models.TextField(null=True)),
                ('contexteduProjet', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Emissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titreEmission', models.CharField(max_length=200)),
                ('EchoEmission', models.FileField(blank=True, null=True, upload_to='Emissions/%Y/%m/%d/')),
                ('texteEmission', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LesEditions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deskEditions', models.CharField(max_length=100)),
                ('dateEditions', models.DateTimeField(auto_now_add=True, verbose_name="date de l'Emission")),
                ('enregistrementJournal', models.FileField(blank=True, null=True, upload_to='jounalsLangues/%Y/%m/%d/')),
            ],
        ),
        migrations.AlterModelOptions(
            name='articles',
            options={'ordering': ['titre', '-date']},
        ),
        migrations.AlterField(
            model_name='articles',
            name='echoArticle',
            field=models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='imageArticle',
            field=models.ImageField(blank=True, null=True, upload_to='Galeries_RMO/'),
        ),
    ]
