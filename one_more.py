import pandas as pd
import requests
import datetime
from functions import *
# Création d'un DataFrame avec les colonnes nécessaires
df = pd.DataFrame(columns=["ville", "temp_actuelle", "temp_ressentie", "temp_min", "temp_max", "pression_atmo", "humidité", "vitesse_vent", "dir_vent", "lever_sol", "coucher_sol"])

# Liste des villes sou variable boa 
boa = ["Gueugnon", "Paris", "Gap", "Albi", "Ajaccio", "Lyon", "Toulouse", "Poitiers", "Troyes", "Biarritz", "Beauvais", "Amiens", "Strasbourg", "Auxerre", "Marseille", "Nice", "Nantes","Dunkerque", "Dieppe","Lorient"]

url="https://api.openweathermap.org/data/2.5/weather"

for i in boa:
    params={
        "q": i,
        "appid": "41a65c4b3f220173fa1f518a942388bc",
        "units": "metric"
    }
    
    response = requests.get(url, params=params)
    response_b = response.json()

    # Récupération des valeurs de température actuelle et de température ressentie
    temp_actuelle = response_b['main']['temp']
    temp_ressentie = response_b['main']['feels_like']
    temp_min = response_b['main']['temp_min']
    temp_max = response_b['main']['temp_max']
    pression_atmo = response_b['main']['pressure']
    humidité = response_b['main']['humidity']
    vitesse_vent = response_b['wind']['speed']
    dir_vent = conversion(response_b['wind']['deg'])
    heure_lever = datetime.datetime.fromtimestamp(response_b['sys']['sunrise'])
    heure_coucher= datetime.datetime.fromtimestamp(response_b['sys']['sunset'])
    lever_sol = heure_lever.time()
    coucher_sol = heure_coucher.time()

    # Ajout des valeurs au DataFrame
    df.loc[len(df)] = [i, temp_actuelle, temp_ressentie, temp_min, temp_max, pression_atmo, humidité, vitesse_vent, dir_vent, lever_sol, coucher_sol]

print(df)
# Affichage du DataFrame mis à jour
df.to_csv("tempile.csv")
