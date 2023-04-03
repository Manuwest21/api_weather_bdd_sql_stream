import sqlite3

connexion = sqlite3.connect("bddeti.db")  

curseur = connexion.cursor() 
#####################################################
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
######################################################
