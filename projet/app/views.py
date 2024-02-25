from .models import fournisseur,client,employe,centre,absence,avanceSalaire,produit,venteProduit,matierePremiere,TransfertMatierePremiere,achat,TransfertMatierePremiere,ReglementFournisseur,VenteMatierePremiere,PaiementCredit,Stock
from .forms import clientForm,fournisseurForm,employeForm,venteProduitForm,produitForm,paiementCredForm,matierePremiereForm,AchatmatierePremiereForm,TransfertmatierePremiereForm,ReglementMPForm,VentematierePremiereForm,PaiementMPForm
from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Sum,ExpressionWrapper,F,FloatField,fields
from django.views.decorators.http import require_GET
from django.http import JsonResponse
from django.utils import timezone

#Home Page
def index(request):
    return render(request,"index.html")
def magasin(request):
    return render(request,"index/Magasin.html")
def centres(request):
    return render(request,"index/Centres.html")
def tableauxDeBord(request):
    return render(request,"index/TableauxDeBord.html")


#Magasin Section
#Gestion Client
def afficher_clients(request):
    if request.method == "GET":
        query = request.GET.get('recherche')
        if query:
            clients=client.objects.filter(nomCl__icontains=query)
        else:
            clients = client.objects.all()
        return render(request,"magasin/client/client.html",{'clients':clients})

def ajouter_client(request):
    if request.method == "POST":
        form=clientForm(request.POST)
        if form.is_valid():
            form.save()
            form=clientForm()
            msg="Client ajoutée avec succès"
            return render(request,"magasin/client/addClient.html",{'form':form,"message":msg})
    else:
        form=clientForm() # créer une instance de formulaire vierge
        msg=""
        return render(request,"magasin/client/addClient.html",{"form":form,"message":msg})

def modifier_client(request,pk):
    cl=client.objects.get(id=pk)
    if request.method == "POST":
        form=clientForm(request.POST,instance=cl)
        if form.is_valid():
            form.save()
            return redirect("liste_clients")
    else:
        form=clientForm(instance=cl)
        return render(request,"magasin/client/editClient.html",{"form":form})

def supprimer_client(request,pk):
    cl = get_object_or_404(client,id=pk)
    if request.method == 'POST':
        cl.delete() 
        return redirect('liste_clients')
    # Si la requête est une GET, afficher la page de confirmation de suppression
    return render(request, 'magasin/client/confirmDelete.html', {'client': cl})

#Gestion Fournisseur
def afficher_fournisseurs(request):
    if request.method == "GET":
        query = request.GET.get('recherche')
        if query:
            fournisseurs=fournisseur.objects.filter(nomF__icontains=query)
        else:
            fournisseurs=fournisseur.objects.all()
        return render(request,"magasin/fournisseur/fournisseur.html",{'fournisseurs':fournisseurs})

def ajouter_fournisseur(request):
    if request.method == "POST":
        form=fournisseurForm(request.POST)
        if form.is_valid():
            form.save()
            form=fournisseurForm()
            msg="Fournisseur ajoutée avec succès"
            return render(request,"magasin/fournisseur/addFournisseur.html",{'form':form,"message":msg})
    else:
        form=fournisseurForm()
        msg=""
        return render(request,"magasin/fournisseur/addFournisseur.html",{"form":form,"message":msg})

def modifier_fournisseur(request,pk):
    f=fournisseur.objects.get(id=pk)
    if request.method == "POST":
        form=fournisseurForm(request.POST,instance=f)
        if form.is_valid():
            form.save()
            return redirect("liste_fournisseurs")
    else:
        form=fournisseurForm(instance=f)
        return render(request,"magasin/fournisseur/editFournisseur.html",{"form":form})

def supprimer_fournisseur(request,pk):
    f=get_object_or_404(fournisseur,id=pk)
    if request.method == 'POST':
        f.delete() 
        return redirect('liste_fournisseurs')
    return render(request,'magasin/fournisseur/confirmDelete.html',{'fournisseur': f})

#Gestion Employe
def afficher_employes(request):
    if request.method == "GET":
        query = request.GET.get('recherche')
        if query:
            employes=employe.objects.filter(nomE__icontains=query)
        else:
            employes=employe.objects.all()
        return render(request,"magasin/employe/employe.html",{'employes':employes})

def ajouter_employe(request):
    if request.method == "POST":
        form=employeForm(request.POST)
        if form.is_valid():
            form.save()
            form=employeForm()
            msg="Employe ajoutée avec succès"
            return render(request,"magasin/employe/addEmploye.html",{'form':form,"message":msg})
    else:
        form=employeForm()
        msg=""
        return render(request,"magasin/employe/addEmploye.html",{"form":form,"message":msg})

def modifier_employe(request,pk):
    e=employe.objects.get(id=pk)
    if request.method == "POST":
        form=employeForm(request.POST,instance=e)
        if form.is_valid():
            form.save()
            return redirect("liste_employes")
    else:
        form=employeForm(instance=e)
        return render(request,"magasin/employe/editEmploye.html",{"form":form})

def supprimer_employe(request,pk):
    e=get_object_or_404(employe,id=pk)
    if request.method == 'POST':
        e.delete() 
        return redirect('liste_employes')
    return render(request,'magasin/employe/confirmDelete.html',{'employe':e})

#Gestion Centre
def afficher_centres(request):
    if request.method == "GET":
        query = request.GET.get('recherche')
        if query:
            centres=centre.objects.filter(nomC__icontains=query)
        else:
            centres = centre.objects.all()
        return render(request,"magasin/centre/centre.html",{'centres':centres})

#Gestion Produit
def afficher_produits(request):
    if request.method == "GET":
        query = request.GET.get('recherche')
        if query:
            produits=produit.objects.filter(nomP__icontains=query)
        else:
            produits = produit.objects.all()
        return render(request,"magasin/produit/produit.html",{'produits':produits})

def ajouter_produit(request):
    if request.method == "POST":
        form=produitForm(request.POST)
        if form.is_valid():
            form.save()
            form=produitForm()
            msg="Produit ajoutée avec succès"
            return render(request,"magasin/produit/addProduit.html",{'form':form,"message":msg})
    else:
        form=produitForm()
        msg=""
        return render(request,"magasin/produit/addProduit.html",{"form":form,"message":msg})

def modifier_produit(request,pk):
    prd=produit.objects.get(id=pk)
    if request.method == "POST":
        form=produitForm(request.POST,instance=prd)
        if form.is_valid():
            form.save()
            return redirect("liste_produits")
    else:
        form=produitForm(instance=prd)
        return render(request,"magasin/produit/editProduit.html",{"form":form})

def supprimer_produit(request,pk):
    prd=get_object_or_404(produit,id=pk)
    if request.method == 'POST':
        prd.delete() 
        return redirect('liste_produits')
    return render(request,'magasin/produit/confirmDelete.html',{'produit':prd})


#Gestion Matiere Premiere
def afficher_matierePremieres(request):
    if request.method == "GET":
        query = request.GET.get('recherche')
        if query:
            produits=produit.objects.filter(nomP__icontains=query)
        else:
            matierePremieres=matierePremiere.objects.all()
        return render(request,"magasin/matierePremiere/matierePremiere.html",{'matierePremieres':matierePremieres})
    
def modifier_matierePremiere(request,pk):
    mp=matierePremiere.objects.get(id=pk)
    if request.method == "POST":
        form=matierePremiereForm(request.POST,instance=mp)
        if form.is_valid():
            form.save()
            return redirect("liste_matierePremieres")
    else:
        form=matierePremiereForm(instance=mp)
        return render(request,"magasin/matierePremiere/editMatierePremiere.html",{"form":form})

def supprimer_matierePremiere(request,pk):
    mp=get_object_or_404(matierePremiere,id=pk)
    if request.method == 'POST':
        mp.delete() 
        return redirect('liste_matierePremieres')
    return render(request,'magasin/matierePremiere/confirmDelete.html',{'matierePremiere':mp})

def ajouter_matierePremiere(request):
    if request.method == "POST":
        form=matierePremiereForm(request.POST)
        if form.is_valid():
            form.save()
            form=matierePremiereForm()
            msg="Matiere Premiere ajoutée avec succès"
            return render(request,"magasin/matierePremiere/addMP.html",{'form':form,"message":msg})
    else:
        form=matierePremiereForm()
        msg=""
        return render(request,"magasin/matierePremiere/addMP.html",{'form':form,"message":msg})
#Achat matiere premiere
def Achat_matierePremiere(request):
    if request.method == "POST":
        form=AchatmatierePremiereForm(request.POST)
        print(form['matieresAchetes'].value()[0])
        if form.is_valid():
            selectedMP = matierePremiere.objects.get(pk=form['matieresAchetes'].value()[0])
            selectedMP.Quantite = selectedMP.Quantite + int(form['QteAchat'].value())
            selectedMP.save()
            solFour = fournisseur.objects.get(pk=form['fournisseur'].value()[0])
            solFour.solde=solFour.solde + float(form['montantRestant'].value())
            solFour.save()

            stock_instance = Stock(
                matierepremier = selectedMP,
                typeTransaction = "achat",
                prix = float(form['prixAchat'].value()),
                QteTransaction = int(form['QteAchat'].value()), 
                montantTransaction = float(form['montantTotal'].value()),
            )
            stock_instance.save()
            form.save()
            form=AchatmatierePremiereForm()
            msg="Achat Matière Première avec succès"
            return render(request,"magasin/matierePremiere/AchatMatierePremiere.html",{'form':form,"message":msg})
        return render(request,"magasin/matierePremiere/AchatMatierePremiere.html",{'form':form,"message":""})
    else:
        form=AchatmatierePremiereForm()
        msg=""
        return render(request,"magasin/matierePremiere/AchatMatierePremiere.html",{"form":form,"message":msg})

#Reglement achat
def ReglementAchat_matierePremiere(request):
    if request.method == "POST":
        form=ReglementMPForm(request.POST)
        if form.is_valid():
            editSoldeF = fournisseur.objects.get(pk=form['Fournisseur'].value()[0])
            editSoldeF.solde = editSoldeF.solde - float(form['montantReg'].value())
            editSoldeF.save()
            form.save()
            form=ReglementMPForm()
            msg="Reglement solde fournisseur avec succès"
            return render(request,"magasin/matierePremiere/ReglementAchat.html",{'form':form,"message":msg})
        return render(request,"magasin/matierePremiere/ReglementAchat.html",{'form':form,"message":""})
    else:
        form=ReglementMPForm()
        msg=""
        return render(request,"magasin/matierePremiere/ReglementAchat.html",{"form":form,"message":msg})


@require_GET
def get_solde(request):
    fournisseur_id = request.GET.get('fournisseur_id')
    solde = fournisseur.objects.get(pk=fournisseur_id).solde
    return JsonResponse({'solde': solde})

# Journal Achat Matiere Premiere
def afficher_JournalAchatMP(request):
    if request.method == "GET":
        MP = request.GET.get('MP')
        dateAchat = request.GET.get('dateAchat')
        fournisseur = request.GET.get('fournisseur')
        QteAchat = request.GET.get('QteAchat')
        prixAchat = request.GET.get('prixAchat')
        sort_by = request.GET.get('sort_by', 'dateAchat')
        filter_query = {}
        if MP:
            filter_query['matieresAchetes__nomMP__icontains']=MP
        if dateAchat:
            filter_query['dateAchat__icontains']=dateAchat
        if fournisseur:
            filter_query['fournisseur__nomF__icontains']=fournisseur
        if QteAchat:
            filter_query['QteAchat__icontains']=QteAchat
        if prixAchat:
            filter_query['prixAchat__icontains']=prixAchat
        achatmatierePremieres=achat.objects.filter(**filter_query).order_by(sort_by)
        sommeachat = achatmatierePremieres.aggregate(total_montant=Sum('montantTotal'))['total_montant']
        return render(request,'magasin/matierePremiere/JournalAchatMP.html',{"achatmatierePremieres":achatmatierePremieres,"sommeachat": sommeachat})

def modifier_AchatmatierePremiere(request,pk):
    mp=achat.objects.get(id=pk)
    if request.method == "POST":
        form=AchatmatierePremiereForm(request.POST,instance=mp)
        if form.is_valid():
            form.save()
            return redirect("liste_AchatmatierePremieres")
    else:
        form=AchatmatierePremiereForm(instance=mp)
        return render(request,"magasin/matierePremiere/EditAchatMatierePremiere.html",{"form":form})
    
def supprimer_AchatmatierePremiere(request,pk):
    mp=get_object_or_404(achat,id=pk)
    sommeachat = 0 
    if request.method == 'POST':
            form=AchatmatierePremiereForm(request.POST)
            matiere_achetee = mp.matieresAchetes  
            if matiere_achetee:
                matiere_achetee.Quantite = matiere_achetee.Quantite - int(mp.QteAchat)
                matiere_achetee.save()
                Stock.objects.filter(
                matierepremier=matiere_achetee,
                typeTransaction="achat",
                prix=float(mp.prixAchat),
                QteTransaction=int(mp.QteAchat),
                montantTransaction=float(mp.montantTotal),).delete()
                mp.delete() 
                EtatStock = Stock.objects.filter(matierepremier=matiere_achetee)
                sommestock = EtatStock.aggregate(
                total_sommestock=Sum(ExpressionWrapper(F('QteTransaction') * F('prix'), output_field=fields.DecimalField()))
            )['total_sommestock'] or 0

            return redirect('liste_AchatmatierePremieres')
    return render(request,'magasin/matierePremiere/DelAchatMatierePremiere.html',{'matierePremiere':mp, 'sommeachat': sommeachat})

# Transfert Matiere Premiere  
def Transfert_matierePremiere(request):
    if request.method == "POST":
        form=TransfertmatierePremiereForm(request.POST)
        if form.is_valid():
            editForm = form.save(commit = False)
            editForm.PrixUTA = achat.objects.get(pk=form['MatieresTransferes'].value()[0]).prixAchat
            editForm.CoutTrf = achat.objects.get(pk=form['MatieresTransferes'].value()[0]).prixAchat * int(form['QteTrf'].value())           
            editForm.save()
            selectedMP = matierePremiere.objects.get(pk=achat.objects.get(pk=form['MatieresTransferes'].value()[0]).matieresAchetes.id)
            selectedMP.Quantite = selectedMP.Quantite - int(form['QteTrf'].value())
            selectedMP.save()
            stock_instance = Stock(
                matierepremier = selectedMP,
                typeTransaction = "Transfert",
                prix = editForm.PrixUTA,
                QteTransaction = int(form['QteTrf'].value()), 
                montantTransaction = editForm.CoutTrf ,
            )
            stock_instance.save()
            form.save()
            form=TransfertmatierePremiereForm()
            msg="Transfert Matière Première avec succès"
            return render(request,"magasin/matierePremiere/TransfertMatierePremiere.html",{'form':form,"message":msg})
        return render(request,"magasin/matierePremiere/TransfertMatierePremiere.html",{'form':form,"message":""})
    else:
        form=TransfertmatierePremiereForm()
        msg=""
        return render(request,"magasin/matierePremiere/TransfertMatierePremiere.html",{"form":form,"message":msg})

# Journal de Transfert Matiere Premiere 
def afficher_JournalTransfertMP(request):
    if request.method == "GET":
        MatieresTransferes = request.GET.get('MatieresTransferes')
        dateTransfert = request.GET.get('dateTransfert')
        centre = request.GET.get('centre')
        QteTrf = request.GET.get('QteTrf')
        PrixUTA = request.GET.get('PrixUTA')
        sort_by = request.GET.get('sort_by', 'dateTransfert')
        filter_query = {}
        if MatieresTransferes:
            filter_query['MatieresTransferes__nomMP__icontains']=MatieresTransferes
        if dateTransfert:
            filter_query['dateTransfert__icontains']=dateTransfert
        if centre:
            filter_query['centre__numeroC__icontains']=client
        if QteTrf:
            filter_query['QteTrf__icontains']=QteTrf
        if PrixUTA:
            filter_query['PrixUTA__icontains']=PrixUTA
        transfertmatierePremieres=TransfertMatierePremiere.objects.filter(**filter_query).order_by(sort_by)
        return render(request,'magasin/matierePremiere/JournalTransfertMP.html',{"transfertmatierePremieres":transfertmatierePremieres})

# Vente Matiere Premiere
def Vente_MatierePremiere(request):
    if request.method == "POST":
        form=VentematierePremiereForm(request.POST)
        print(form['MPVendus'].value()[0])
        if form.is_valid():
            selectedMP = matierePremiere.objects.get(pk=form['MPVendus'].value()[0])
            selectedMP.Quantite = selectedMP.Quantite - int(form['QteVds'].value())
            selectedMP.save()
            credCL = client.objects.get(pk=form['client'].value()[0])
            credCL.credit=credCL.credit + int(form['ResteAPayer'].value())
            credCL.save()
            stock_instance = Stock(
                matierepremier = selectedMP,
                typeTransaction = "Vente",
                prix = float(form['prixUT'].value()),
                QteTransaction = int(form['QteVds'].value()), 
                montantTransaction = float(form['montantVente'].value()),
            )
            stock_instance.save()
            form.save()
            form=VentematierePremiereForm()
            msg="Vente Matière Première avec succès"
            return render(request,"magasin/matierePremiere/VenteMatierePremiere.html",{'form':form,"message":msg})
        return render(request,"magasin/matierePremiere/VenteMatierePremiere.html",{'form':form,"message":""})
    else:
        form=VentematierePremiereForm()
        msg=""
        return render(request,"magasin/matierePremiere/VenteMatierePremiere.html",{"form":form,"message":msg})

def PaiementCredit_matierePremiere(request):
    if request.method == "POST":
        form=PaiementMPForm(request.POST)
        if form.is_valid():
            editCreditCl = client.objects.get(pk=form['client'].value()[0])
            editCreditCl.credit = editCreditCl.credit - float(form['montantPayMP'].value())
            editCreditCl.save()
            form.save()
            form=PaiementMPForm()
            msg="Paiement Credit Reglé avec succès"
            return render(request,"magasin/matierePremiere/PaiementCredit.html",{'form':form,"message":msg})
        return render(request,"magasin/matierePremiere/PaiementCredit.html",{'form':form,"message":""})
    else:
        form=PaiementMPForm()
        msg=""
        return render(request,"magasin/matierePremiere/PaiementCredit.html",{"form":form,"message":msg})


@require_GET
def get_credit(request):
    client_id = request.GET.get('client_id')
    credit = client.objects.get(pk=client_id).credit
    return JsonResponse({'credit': credit})

#Journal de Vente Matiere Premiere 
def afficher_JournalVenteMP(request):
    if request.method == "GET":
        MPVendus = request.GET.get('MPVendus')
        dateVente = request.GET.get('dateVente')
        client = request.GET.get('client')
        QteVds = request.GET.get('QteVds')
        prixUT = request.GET.get('prixUT')
        sort_by = request.GET.get('sort_by', 'dateVente')
        filter_query = {}
        if MPVendus:
            filter_query['MPVendus__nomMP__icontains']=MPVendus
        if dateVente:
            filter_query['dateVente__icontains']=dateVente
        if client:
            filter_query['client__nomCl__icontains']=client
        if QteVds:
            filter_query['QteVds__icontains']=QteVds
        if prixUT:
            filter_query['prixUT__icontains']=prixUT
        ventematierePremieres=VenteMatierePremiere.objects.filter(**filter_query).order_by(sort_by)
        sommeVente = ventematierePremieres.aggregate(total_montant=Sum('montantVente'))['total_montant']
        sommeencais = ventematierePremieres.aggregate(total_encais=Sum('montantEncaisse'))['total_encais']
        return render(request,'magasin/matierePremiere/JournalVenteMP.html',{"ventematierePremieres":ventematierePremieres,'sommeVente': sommeVente,'sommeencais':sommeencais})

def modifier_VentematierePremiere(request,pk):
    mp=VenteMatierePremiere.objects.get(id=pk)
    if request.method == "POST":
        form=VentematierePremiereForm(request.POST,instance=mp)
        if form.is_valid():
            form.save()
            return redirect("liste_VentematierePremieres")
    else:
        form=VentematierePremiereForm(instance=mp)
        return render(request,"magasin/matierePremiere/EditVenteMatierePremiere.html",{"form":form})

def supprimer_VentematierePremiere(request,pk):
    mp=get_object_or_404(VenteMatierePremiere,id=pk)
    if request.method == 'POST':
            form=VentematierePremiereForm(request.POST)
            matiere_vendu = mp.MPVendus 
            if matiere_vendu:
                matiere_vendu.Quantite = matiere_vendu.Quantite - int(mp.QteVds)
                matiere_vendu.save()
                total_vente = Stock.objects.filter(
                matierepremier=matiere_vendu,
                typeTransaction="Vente",
                prix=float(mp.prixUT),
                QteTransaction=int(mp.QteVds),
                montantTransaction=float(mp.montantVente),
            ).aggregate(
                total_vente=Sum(ExpressionWrapper(F('QteTransaction') * F('prix'), output_field=fields.DecimalField()))
            )['total_vente'] or 0
            Stock.objects.filter(
                matierepremier=matiere_vendu,
                typeTransaction="Vente",
                prix=float(mp.prixUT),
                QteTransaction=int(mp.QteVds),
                montantTransaction=float(mp.montantVente),
            ).delete()
            EtatStock = Stock.objects.filter(matierepremier=matiere_vendu)
            sommestock = EtatStock.aggregate(
                total_sommestock=Sum(ExpressionWrapper(F('QteTransaction') * F('prix'), output_field=fields.DecimalField()))
            )['total_sommestock'] or 0
            mp.delete()
            return redirect('liste_VentematierePremieres')
    return render(request,'magasin/matierePremiere/DelAchatMatierePremiere.html',{'matierePremiere':mp})

# Afficher Etat Stock
def afficher_etatStock(request):
    if request.method == "GET":
        matierepremier = request.GET.get('matierepremier')
        typeTransaction = request.GET.get('typeTransaction')
        prix = request.GET.get('prix')
        QteTransaction = request.GET.get('QteTransaction')
        montantTransaction = request.GET.get('montantTransaction')
        filter_query = {}
        if matierepremier:
            filter_query['matierepremier__icontains']=matierepremier
        if typeTransaction:
            filter_query['typeTransaction__icontains']=typeTransaction
        if prix:
            filter_query['prix__icontains']=prix
        if QteTransaction:
            filter_query['QteTransaction__icontains']=QteTransaction
        if montantTransaction:
            filter_query['montantTransaction__icontains']=montantTransaction
        EtatStock =Stock.objects.filter(**filter_query)
        total_achat = 0
        total_vente = 0
        total_transfert = 0
        quantite_achat = 0
        quantite_vente = 0
        quantite_transfert = 0

        for stock_entry in EtatStock:
            if stock_entry.typeTransaction == 'achat':
                total_achat += stock_entry.QteTransaction * stock_entry.prix
                quantite_achat += stock_entry.QteTransaction
            elif stock_entry.typeTransaction == 'Vente':
                total_vente += stock_entry.QteTransaction * stock_entry.prix
                quantite_vente += stock_entry.QteTransaction
            elif stock_entry.typeTransaction == 'Transfert':
                total_transfert += stock_entry.QteTransaction * stock_entry.prix
                quantite_transfert += stock_entry.QteTransaction
        sortie_stock = quantite_vente + quantite_transfert       
        total_stock = total_vente - total_achat
        QteStock = quantite_achat - sortie_stock
        return render(request, "magasin/matierePremiere/EtatStock.html", {
            'EtatStock': EtatStock,
            'total_achat': total_achat,
            'total_vente': total_vente,
            'total_transfert': total_transfert,
            'quantite_achat': quantite_achat,
            'quantite_vente': quantite_vente,
            'quantite_transfert': quantite_transfert,
            'total_stock': total_stock,
            'QteStock': QteStock
        })
    return render(request, "magasin/matierePremiere/EtatStock.html", {'EtatStock': []})

#Centre Section
def section_centre(request,centre_id):
    centre_id=centre_id
    return render(request,"centre/modules.html",{'centre_id':centre_id})

#Activités du Centre
def activites_centre(request,centre_id):
    return render(request,"centre/activitesCentre.html",{'centre_id':centre_id})

#Journal des Transferts
def journal_transfert(request,centre_id):
    if request.method == "GET":
        sort_by = request.GET.get('sort_by','dateTransfert')
        c=centre.objects.get(numeroC=centre_id)
        query=request.GET.get('recherche')
        queryDateMin=request.GET.get('dateMin')
        queryDateMax=request.GET.get('dateMax')

        if query:
            transferts=TransfertMatierePremiere.objects.filter(MatieresTransferes__nomMP__icontains=query,centre=c).order_by(sort_by)
        elif (queryDateMin and queryDateMax):
            transferts=TransfertMatierePremiere.objects.filter(dateTransfert__range=[queryDateMin,queryDateMax],centre=c).order_by(sort_by)
        else:
            transferts=TransfertMatierePremiere.objects.filter(centre=c).order_by(sort_by)

        sommeTransferts=0
        for t in transferts:
            sommeTransferts+=t.CoutTrf
        return render(request,"centre/journal_transfert.html",{'transferts':transferts,'centre_id':centre_id,'somme_transferts':sommeTransferts})

#Ventes des Produits
def journal_vente(request,centre_id):
    transferts=None
    if request.method == "GET":
        sort_by_vente = request.GET.get('sort_by','dateVente')
        sort_by_transfert = request.GET.get('sort_by','dateTransfert')
        c=centre.objects.get(numeroC=centre_id)
        query=request.GET.get('recherche')
        queryClient=request.GET.get('clientName')
        queryDateMin=request.GET.get('dateMin')
        queryDateMax=request.GET.get('dateMax')

        if query:
            ventes=venteProduit.objects.filter(produitVendu__nomP__icontains=query,centre=c).order_by(sort_by_vente)
        elif queryClient:
            ventes=venteProduit.objects.filter(client__nomCl__icontains=queryClient,centre=c).order_by(sort_by_vente)
        elif (queryDateMin and queryDateMax):
            ventes=venteProduit.objects.filter(dateVente__range=[queryDateMin,queryDateMax],centre=c).order_by(sort_by_vente)
            transferts=TransfertMatierePremiere.objects.filter(dateTransfert__range=[queryDateMin,queryDateMax],centre=c).order_by(sort_by_transfert)
        else:
            ventes=venteProduit.objects.filter(centre=c).order_by(sort_by_vente)
            transferts=TransfertMatierePremiere.objects.filter(centre=c).order_by(sort_by_transfert)

        sommeTransferts=0
        if transferts:
            for t in transferts:
                sommeTransferts+=t.CoutTrf

        sommeVentes=0
        for v in ventes:
            v.montantTotal = v.qteVendu * v.prixVente
            sommeVentes+=v.montantTotal
            
        benefice=sommeVentes-sommeTransferts
        return render(request,"centre/journal_vente.html",{'ventes':ventes,'centre_id':centre_id,'somme_ventes':sommeVentes,'benefice':benefice})
    return render(request,"centre/journal_vente.html",{'centre_id':centre_id})

def ajouter_vente(request,centre_id):
    if request.method == "POST":
        form=venteProduitForm(request.POST)
        msg_montant=""
        if form.is_valid():
            c=centre.objects.get(numeroC=centre_id)
            form.instance.centre=c

            id_prd=request.POST.get("produitVendu")
            prd=produit.objects.get(id=id_prd)
            qte=int(request.POST.get("qteVendu"))
            if(prd.qte>=qte):
                prix=float(request.POST.get("prixVente"))
                montant_total=qte*prix
                msg_montant="Montant Total ="+str(montant_total)

                prd.qte-=qte
                prd.save()

                montant_verse=float(request.POST.get("montantVerse"))
                if(montant_verse==0):
                    form.instance.montantVerse=montant_total
                else:
                    id_cl=request.POST.get("client")
                    cl=client.objects.get(id=id_cl)
                    montant_restant=montant_total-montant_verse
                    cl.credit=montant_restant
                    cl.save()
                
                form.save()
                form=venteProduitForm()
                msg="Vente enregistrée avec succès"
            else:
                msg="Stock inssufisant, Quantité en stock= "+str(prd.qte)

            return render(request,"centre/addVente.html",{'form':form,"message":msg,'centre_id':centre_id,'message_montant':msg_montant})
    else:
        form=venteProduitForm()
        msg=""
        return render(request,"centre/addVente.html",{"form":form,"message":msg,'centre_id':centre_id})
    
#Paiement Crédit Client
def paiement_credit(request, centre_id):
    cl = None
    form = paiementCredForm()
    msg = ""

    if request.method == "POST":
        query = request.POST.get('search')
        if query:
            cl = client.objects.get(nomCl__icontains=query)
        
        form = paiementCredForm(request.POST)
        if form.is_valid():
            if cl:
                montant_paiement=request.POST.get("montantPaiement")
                if montant_paiement:
                    cl.credit-=float(montant_paiement)
                    cl.save()
                    form.instance.client = cl
                    form.save()
                    msg = "Paiement effectué avec succès"
                    form = paiementCredForm()
            else:
                msg="Client non trouvé"

    return render(request, "centre/paiementCredit.html", {'form': form, "message": msg, 'centre_id': centre_id, 'cl': cl})

#Module Employé
def module_employe(request,centre_id):
    c=centre.objects.get(numeroC=centre_id)
    employes=employe.objects.filter(centre=c)
    return render(request,"centre/moduleEmploye.html",{'centre_id':centre_id,'employes':employes})

#Syteme Pointage
def modifier_points(request,pk):
    msg=""
    e=employe.objects.get(id=pk)
    if request.method == "POST":
        new_points=request.POST.get("points")
        if new_points is not None and new_points.isdigit():
            e.points=int(new_points)
            e.save()
            return redirect("module_employe",centre_id=e.centre.numeroC)
        else:
            msg="Valeur de Points invalide"
            return render(request,"centre/editPoints.html",{"employe":e,"message":msg})
    else:
        return render(request,"centre/editPoints.html",{"employe":e,"message":msg})

#Systeme Absence
def afficher_absence(request,pk):
    e=employe.objects.get(id=pk)
    absences=absence.objects.filter(employe=pk)
    return render(request,"centre/absences.html",{'absences':absences,'employe':e})

def ajouter_absence(request,employe_id):
    msg=""
    if request.method == "POST":
        date_absence=request.POST.get("dateAbsence")
        e=employe.objects.get(id=employe_id)
        absence.objects.create(employe=e,dateAbsence=date_absence)
        msg="Absence ajoutée avec succès"
    return render(request,"centre/addAbsence.html",{'employe_id':employe_id,"message":msg})

def modifier_absence(request,pk):
    a=absence.objects.get(id=pk)
    if request.method == "POST":
        a.dateAbsence=request.POST.get("dateAbsence")
        a.save()
        return redirect("absence",pk=a.employe.id)
    else:
        date_absence=a.dateAbsence.strftime('%Y-%m-%d') #Format the date for display
        return render(request,"centre/editAbsence.html",{'absence':a,'dateAbsence':date_absence})

def supprimer_absence(request,pk):
    a=get_object_or_404(absence,id=pk)
    if request.method == 'POST':
        a.delete() 
        return redirect("absence",pk=a.employe.id)
    return render(request,'centre/deleteAbsence.html',{'absence':a})

#Systeme Avance Salaire
def afficher_avanceSalaire(request,pk):
    e=employe.objects.get(id=pk)
    avanceSalaires=avanceSalaire.objects.filter(employe=pk)
    return render(request,"centre/avanceSalaire.html",{'avanceSalaires':avanceSalaires,'employe':e})

def ajouter_avanceSalaire(request,employe_id):
    msg=""
    if request.method == 'POST':
        montant=request.POST.get('montant')
        date_avanceSalaire=request.POST.get('dateAvanceSalaire')
        e=employe.objects.get(id=employe_id)
        avanceSalaire.objects.create(employe=e,montant=montant,dateDemande=date_avanceSalaire)
        msg="Demande ajoutée avec succès"
    return render(request,"centre/addAvanceSalaire.html",{'employe_id':employe_id,"message":msg})

def modifier_avanceSalaire(request,pk):
    avanceS=avanceSalaire.objects.get(id=pk)
    if request.method == "POST":
        avanceS.montant=request.POST.get("montant")
        avanceS.dateDemande=request.POST.get("dateAvanceSalaire")
        avanceS.save()
        return redirect("avanceSalaire",pk=avanceS.employe.id)
    else:
        date_avanceSalaire=avanceS.dateDemande.strftime('%Y-%m-%d')
        return render(request,"centre/editAvanceSalaire.html",{'avanceSalaire':avanceS,'dateAvanceSalaire':date_avanceSalaire,'montant':avanceS.montant})

def supprimer_avanceSalaire(request,pk):
    avanceS=get_object_or_404(avanceSalaire,id=pk)
    if request.method == "POST":
        avanceS.delete()
        return redirect("avanceSalaire",pk=avanceS.employe.id)
    return render(request,"centre/delteAvanceSalaire.html",{'avanceSalaire':avanceS})


#Tableux de Bord Section
def analyse_vente(request):
    return render(request,'tableauxDeBord/optionsCentres.html')

def afficher_tableaux(request,centre_id):
    if request.method == "GET":
        queryAnneeMin=request.GET.get('anneeMin')
        queryAnneeMax=request.GET.get('anneeMax')
        if (queryAnneeMin and queryAnneeMax):
            anneeMin=int(queryAnneeMin)
            anneeMax=int(queryAnneeMax)
            annees=range(anneeMin,anneeMax+1)

            if(centre_id != 0):
                c=centre.objects.get(numeroC=centre_id)
                ventes=venteProduit.objects.filter(dateVente__year__range=(anneeMin,anneeMax),centre=c)
                ventesAnneePrecedante=venteProduit.objects.filter(dateVente__year__range=(anneeMin-(anneeMax-anneeMin+1),anneeMin-1),centre=c)
                transferts=TransfertMatierePremiere.objects.filter(dateTransfert__year__range=(anneeMin,anneeMax),centre=c)
                transfertsAnneePrecedante=TransfertMatierePremiere.objects.filter(dateTransfert__year__range=(anneeMin-(anneeMax-anneeMin+1),anneeMin-1),centre=c)
                produits=produit.objects.filter(
                    venteproduit__dateVente__year__range=(anneeMin,anneeMax),venteproduit__centre=c
                ).annotate(qte_sold=Sum('venteproduit__qteVendu')
                ).order_by('-qte_sold')[:10]
                clients=client.objects.filter(
                    venteproduit__dateVente__year__range=(anneeMin,anneeMax),venteproduit__centre=c
                ).annotate(
                    total_sale=Sum(ExpressionWrapper(F('venteproduit__qteVendu') * F('venteproduit__prixVente'),output_field=FloatField()))
                ).order_by('-total_sale')[:10]
            else:
                ventes=venteProduit.objects.filter(dateVente__year__range=(anneeMin,anneeMax))
                ventesAnneePrecedante=venteProduit.objects.filter(dateVente__year__range=(anneeMin-(anneeMax-anneeMin+1),anneeMin-1))
                transferts=TransfertMatierePremiere.objects.filter(dateTransfert__year__range=(anneeMin,anneeMax))
                transfertsAnneePrecedante=TransfertMatierePremiere.objects.filter(dateTransfert__year__range=(anneeMin-(anneeMax-anneeMin+1),anneeMin-1))
                produits=produit.objects.filter(
                    venteproduit__dateVente__year__range=(anneeMin,anneeMax)
                ).annotate(qte_sold=Sum('venteproduit__qteVendu')
                ).order_by('-qte_sold')[:10]
                clients=client.objects.filter(
                    venteproduit__dateVente__year__range=(anneeMin,anneeMax)
                ).annotate(
                    total_sale=Sum(ExpressionWrapper(F('venteproduit__qteVendu') * F('venteproduit__prixVente'),output_field=FloatField()))
                ).order_by('-total_sale')[:10]


            totalVentes=ventes.aggregate(total_ventes=Sum(ExpressionWrapper(F('qteVendu') * F('prixVente'),output_field=FloatField())))['total_ventes'] or 0
            totalVentesAnneePrecedante=ventesAnneePrecedante.aggregate(total_ventes_annee_precedante=Sum(ExpressionWrapper(F('qteVendu') * F('prixVente'),output_field=FloatField())))['total_ventes_annee_precedante'] or 0
            if totalVentesAnneePrecedante > 0:
                tauxVentes=((totalVentes-totalVentesAnneePrecedante)/totalVentesAnneePrecedante)*100
            else:
                tauxVentes=100

            totalTransferts=transferts.aggregate(total_transferts=Sum('CoutTrf'))['total_transferts'] or 0
            totalTransfertsAnneePrecedante=transfertsAnneePrecedante.aggregate(total_transferts_annee_precedante=Sum('CoutTrf'))['total_transferts_annee_precedante'] or 0

            totalBenefice=totalVentes-totalTransferts
            totalBeneficeAnneePrecedante=totalVentesAnneePrecedante-totalTransfertsAnneePrecedante
            if totalBeneficeAnneePrecedante > 0:
                tauxBenefice=((totalBenefice-totalBeneficeAnneePrecedante)/totalBeneficeAnneePrecedante)*100
            else:
                tauxBenefice=100
            return render(request,'tableauxDeBord/tableaux.html',{'centre_id':centre_id,'annees':annees,'taux_ventes':tauxVentes,'taux_benefice':tauxBenefice,'ventes':ventes,'produits':produits,'clients':clients})
    return render(request,'tableauxDeBord/tableaux.html',{'centre_id':centre_id})


def afficher_tableaux_achat(request):
    if request.method == "GET":
        queryAnneeMin = request.GET.get('anneeMin')
        queryAnneeMax = request.GET.get('anneeMax')

        if queryAnneeMin and queryAnneeMax:
            anneeMin = int(queryAnneeMin)
            anneeMax = int(queryAnneeMax)
            annees = range(anneeMin, anneeMax + 1)

            total_achats = achat.objects.filter(dateAchat__year__range=(anneeMin, anneeMax))\
                .aggregate(total=Sum('montantTotal'))['total'] or 0

            previous_year_start = timezone.now() - timezone.timedelta(days=365)
            total_previous_year = achat.objects.filter(dateAchat__year__range=(previous_year_start.year, previous_year_start.year))\
                .aggregate(total=Sum('montantTotal'))['total'] or 0

            taux_evolution = ((total_achats - total_previous_year) / total_previous_year) * 100 if total_previous_year > 0 else 100
            top_fournisseurs = achat.objects.filter(dateAchat__year__range=(anneeMin, anneeMax))\
                .values('fournisseur__nomF')\
                .annotate(total_achats=Sum('montantTotal'))\
                .order_by('-total_achats')[:5]

            return render(request, 'tableauxDeBord/tableauachat.html', {
                'taux_evolution': taux_evolution,
                'top_fournisseurs': top_fournisseurs,
                'annees': annees,
            })

    return render(request, 'tableauxDeBord/tableauachat.html')