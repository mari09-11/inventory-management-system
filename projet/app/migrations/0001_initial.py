# Generated by Django 5.0 on 2024-01-22 15:44

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='centre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomC', models.CharField(max_length=50)),
                ('numeroC', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3')], unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomCl', models.CharField(max_length=50)),
                ('prenomCl', models.CharField(max_length=50)),
                ('adresseCl', models.CharField(max_length=50)),
                ('telephoneCl', models.CharField(max_length=10)),
                ('credit', models.FloatField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='fournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomF', models.CharField(max_length=50)),
                ('prenomF', models.CharField(max_length=50)),
                ('adresseF', models.CharField(max_length=50)),
                ('telephoneF', models.CharField(max_length=10)),
                ('solde', models.FloatField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomP', models.CharField(max_length=50)),
                ('qte', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matierepremier', models.CharField(max_length=50)),
                ('typeTransaction', models.CharField(max_length=50)),
                ('prix', models.FloatField(default=0)),
                ('QteTransaction', models.IntegerField()),
                ('montantTransaction', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomE', models.CharField(max_length=50)),
                ('prenomE', models.CharField(max_length=50)),
                ('adresseE', models.CharField(max_length=50)),
                ('telephoneE', models.CharField(max_length=10)),
                ('salaire_jour', models.FloatField(max_length=10)),
                ('points', models.IntegerField(default=0)),
                ('centre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.centre')),
            ],
        ),
        migrations.CreateModel(
            name='avanceSalaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('montant', models.FloatField()),
                ('dateDemande', models.DateField()),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employe')),
            ],
        ),
        migrations.CreateModel(
            name='absence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateAbsence', models.DateField()),
                ('employe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employe')),
            ],
        ),
        migrations.CreateModel(
            name='matierePremiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomMP', models.CharField(max_length=50)),
                ('TypeMP', models.CharField(max_length=50)),
                ('Quantite', models.IntegerField()),
                ('Fournisseur', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.fournisseur')),
            ],
        ),
        migrations.CreateModel(
            name='achat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateAchat', models.DateTimeField(default=datetime.datetime.now)),
                ('QteAchat', models.IntegerField(default=0)),
                ('prixAchat', models.FloatField(default=0)),
                ('montantTotal', models.FloatField(default=0)),
                ('montantverse', models.FloatField(default=0)),
                ('montantRestant', models.FloatField(default=0)),
                ('fournisseur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.fournisseur')),
                ('matieresAchetes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.matierepremiere')),
            ],
        ),
        migrations.CreateModel(
            name='paiementCred',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datePaiement', models.DateTimeField(default=datetime.datetime.now)),
                ('montantPaiement', models.FloatField(blank=True, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.client')),
            ],
        ),
        migrations.CreateModel(
            name='PaiementCredit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DatePventeMP', models.DateTimeField(default=datetime.datetime.now)),
                ('credit', models.FloatField(default=0)),
                ('montantPayMP', models.FloatField(default=0)),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.client')),
            ],
        ),
        migrations.CreateModel(
            name='ReglementFournisseur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateReg', models.DateTimeField(default=datetime.datetime.now)),
                ('solde', models.FloatField(default=0)),
                ('montantReg', models.FloatField(default=0)),
                ('Fournisseur', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.fournisseur')),
            ],
        ),
        migrations.CreateModel(
            name='TransfertMatierePremiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTransfert', models.DateTimeField(default=datetime.datetime.now)),
                ('QteTrf', models.IntegerField()),
                ('PrixUTA', models.FloatField(default=0)),
                ('CoutTrf', models.IntegerField(default=0)),
                ('MatieresTransferes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.matierepremiere')),
                ('centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.centre')),
            ],
        ),
        migrations.CreateModel(
            name='VenteMatierePremiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateVente', models.DateTimeField(default=datetime.datetime.now)),
                ('QteVds', models.IntegerField(default=0)),
                ('prixUT', models.FloatField(default=0)),
                ('montantVente', models.FloatField(default=0)),
                ('montantEncaisse', models.FloatField(default=0)),
                ('ResteAPayer', models.FloatField(default=0)),
                ('MPVendus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.matierepremiere')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.client')),
            ],
        ),
        migrations.CreateModel(
            name='venteProduit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateVente', models.DateTimeField(default=datetime.datetime.now)),
                ('qteVendu', models.IntegerField()),
                ('prixVente', models.FloatField(max_length=10)),
                ('montantVerse', models.FloatField(default=0)),
                ('centre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.centre')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.client')),
                ('produitVendu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.produit')),
            ],
        ),
    ]
