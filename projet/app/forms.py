from django.db.models import fields
from django import forms
from .models import client,fournisseur,centre,employe,produit,venteProduit,paiementCred,matierePremiere,achat,TransfertMatierePremiere,ReglementFournisseur,VenteMatierePremiere,PaiementCredit,Stock
import calculation 
from django_select2 import forms as s2forms


centre_possibles=[
        (1, '1'),
        (2, '2'),
        (3, '3')
    ]

class clientForm(forms.ModelForm):
    class Meta:
        model = client
        exclude=['credit']
        labels = {
            'nomCl': 'Nom',
            'prenomCl': 'Prénom',
            'adresseCl': 'Adresse',
            'telephoneCl': 'Telephone'
        }

class fournisseurForm(forms.ModelForm):
    class Meta:
        model = fournisseur
        exclude=['solde']
        labels = {
            'nomF': 'Nom',
            'prenomF': 'Prénom',
            'adresseF': 'Adresse',
            'telephoneF': 'Telephone'
        }

class employeForm(forms.ModelForm):
    class Meta:
        model = employe
        exclude=['points']
        labels = {
            'nomE': 'Nom',
            'prenomE': 'Prénom',
            'adresseE': 'Adresse',
            'telephoneE': 'Telephone',
            'salaire_jour': 'Salaire journalier',
            'centre': 'Centre'
        }

class produitForm(forms.ModelForm):
    class Meta:
        model=produit
        fields="__all__"
        labels = {
            'nomP': 'Nom produit',
            'qte':'Quantité',
        }

class venteProduitForm(forms.ModelForm):
    class Meta:
        model=venteProduit
        exclude=['centre']
        labels={
            'dateVente':'Date',
            'produitVendu':'Produit',
            'qteVendu':'Quantité',
            'prixVente':'Prix Unitaire',
            'montantVerse':'Montant Versé'
        }

class paiementCredForm(forms.ModelForm):
    class Meta:
        model=paiementCred
        exclude=['client']
        labels={
            'datePaiement':'Date',
            'montantPaiement':'Montant du Paiement'
        }

class matierePremiereForm(forms.ModelForm):
    class Meta:
        model=matierePremiere
        fields=['nomMP','TypeMP']
        labels={
            'nomMP':'Nom matiere premiere',
            'TypeMP':'Type',
        }

class fournisseurWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "nomF__icontains",
    ]


class matieresAchetesWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "nomMP__icontains",
    ]

class AchatmatierePremiereForm(forms.ModelForm): 
    montantTotal=forms.IntegerField(widget=calculation.FormulaInput('QteAchat*prixAchat', attrs={'readonly': 'readonly'}),label='Montant Total',disabled=False, required=False  )
    montantRestant=forms.IntegerField(widget=calculation.FormulaInput('montantTotal - montantverse', attrs={'readonly': 'readonly'}),label='Montant Restant',disabled=False, required=False  )
    class Meta:
        model = achat
        fields="__all__"
        widgets = {
            "fournisseur": fournisseurWidget(attrs={'required': False}), 
            "matieresAchetes": matieresAchetesWidget,
        }

class matierestransfertWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "matieresAchetes__nomMP__icontains",
    ]
class TransfertmatierePremiereForm(forms.ModelForm):
    centre=centre.numeroC
    PrixUTA = forms.FloatField(widget=forms.HiddenInput(),label='Cout de Transfert',disabled=False, required=False  )
    CoutTrf=forms.IntegerField(widget=forms.HiddenInput(),label='Cout de Transfert',disabled=False, required=False)
    class Meta:
        model = TransfertMatierePremiere
        fields="__all__"
        labels = {
            'dateTransfert': 'Date Transfert',
            'centre': 'Numero centre',
            'MatieresTransferes': 'Matieres Transferes',
            'QteTrf':'Quantité',
            'PrixUTA':'Prix Unitaire',
            'CoutTrf':'Cout de Transfert'
        }

        widgets = {
            "MatieresTransferes": matierestransfertWidget,
        }

    
class fournisseurregWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "nomF__icontains",
    ]
class ReglementMPForm(forms.ModelForm):
    class Meta:
        model = ReglementFournisseur
        fields="__all__"        
        widgets = {
            "Fournisseur": fournisseurregWidget, 
        }

    def __init__(self, *args, **kwargs):
        super(ReglementMPForm, self).__init__(*args, **kwargs)
        self.fields['solde'].widget.attrs['readonly'] = True
        self.fields['Fournisseur'].initial = None
        self.fields['Fournisseur'].widget.attrs['class'] = 'fournisseur-dropdown'


class matieresVendueWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "nomMP__icontains",
    ]

class VentematierePremiereForm(forms.ModelForm):
    montantVente=forms.FloatField(widget=calculation.FormulaInput('QteVds*prixUT', attrs={'readonly': 'readonly'}),label='Montant Total',disabled=False, required=False  )
    ResteAPayer=forms.FloatField(widget=calculation.FormulaInput('montantVente - montantEncaisse', attrs={'readonly': 'readonly'}),label='Montant Restant',disabled=False, required=False  )

    
    class Meta:
        model = VenteMatierePremiere
        fields="__all__"
        labels = {
            'dateVente': 'Date de Vente',
            'client': 'Nom Client',
            'MPVendus': 'Matiere Premiere',
            'QteVds': 'Quantite vendue',
            'prixUT': 'Prix de Vente',
            'montantVente': 'Montant de Vente',
            'montantEncaisse':'Montant Encaissé',
            'ResteAPayer': 'Reste à payer',
        }

        widgets = {
            "MPVendus": matieresVendueWidget,
        }

class clientWidget(s2forms.ModelSelect2Widget):
    search_fields = [
        "nomCl__icontains",
    ]

class PaiementMPForm(forms.ModelForm):
    class Meta:
        model = PaiementCredit
        fields="__all__"      
        labels = {
            'DatePventeMP ': 'Date de Vente',
            'client': 'Nom Client',
            'credit': 'Credit',
            'montantPayMP': 'Montant Paiement',
          }  
        widgets = {
            "client": clientWidget, 
        }
        
def __init__(self, *args, **kwargs):
    super(PaiementMPForm, self).__init__(*args, **kwargs)
    self.fields['credit'].widget.attrs['readonly'] = True
    self.fields['client'].initial = None
    self.fields['client'].widget.attrs['class'] = 'client-dropdown'

    