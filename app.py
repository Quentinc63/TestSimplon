import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure.write_html('ventes-par-region.html')


print('ventes-par-région.html généré avec succès !')



px.pie(données.groupby('produit', as_index=False).sum()
       , values='qte', names='produit', title='quantité vendue par produit').write_html('ventes-par-produit.html')


chiffre_affaire_produit = données.assign(chiffre_affaires=données['prix'] * données['qte']).groupby('produit', as_index=False)['chiffre_affaires'].sum()

px.pie(chiffre_affaire_produit, values='chiffre_affaires', names='produit', title="chiffre d'affaires par produit").write_html('chiffre-affaire-par-produit.html')