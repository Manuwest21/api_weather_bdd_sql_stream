import csv
import sqlite3
import pandas as pd
# Se connecter à la base de données
connexion = sqlite3.connect("bddetis.db")
curseur = connexion.cursor()

# Créer la table villes si elle n'existe pas déjà
curseur.execute(""" 
       CREATE TABLE IF NOT EXISTS villes(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          ville TEXT NOT NULL,
          temp_actuelle TEXT NOT NULL ,
          temp_ressentie TEXT NOT NULL,
          temp_min TEXT NOT NULL,
          temp_max TEXT NOT NULL,
          pression_atmo TEXT NOT NULL,
          humidité TEXT NOT NULL,
          vitesse_vent TEXT NOT NULL,
          dir_vent TEXT NOT NULL,
          lever_sol TEXT NOT NULL,
          coucher_sol TEXT NOT NULL
            )
""")
connexion.commit()

# #Lire les données CSV et les insérer dans la base de données
# with open('tempile.csv', 'r') as f:
#     lecteur_csv = csv.reader(f, delimiter=',')
#     next(lecteur_csv)  # Skip la première ligne (les noms de colonnes)
#     for ligne in lecteur_csv:
#         # Transformer la ligne CSV en tuple
#         donnees_ville = tuple(ligne)

#         # Insérer le tuple dans la table villes
#         curseur.execute("""
#             INSERT INTO villes(ville,temp_actuelle,temp_ressentie,temp_min,temp_max,pression_atmo,humidité,vitesse_vent,dir_vent,lever_sol,coucher_sol)
#             VALUES (?,?,?,?,?,?,?,?,?,?,?,?)
#         """, donnees_ville)




df=pd.read_csv('tempile.csv')

conect= sqlite3.connect("bddeti.db")


df.to_sql('villes', conect, if_exists='replace', index=False)

conect.close()

