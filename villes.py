import pandas as pd
import requests

# Création d'un DataFrame vide avec les colonnes nécessaires
   # lever_sol=['sys']['sunrise']
df = pd.DataFrame(columns=["ville", "temp_actuelle", "temp_ressentie","temp_min","temp_max","pression_atmo","humidité","vitesse_vent","dir_vent","lever_sol","coucher_sol"])

# Liste de villes à interroger
boa = ["Gueugnon", "Paris", "Gap","Albi","Ajaccio","Lyon","Toulouse","Poitiers","Troyes","Biarritz", "Beauvais","Amiens", "Strasbourg","Auxerre","Marseille", "Nice", "Nantes"]

url="https://api.openweathermap.org/data/2.5/weather"

for i in boa:
    params={
        "q":i,
        "appid": "41a65c4b3f220173fa1f518a942388bc",
        "units": "metric"
    }
    response = requests.get(url, params=params)
    response_b = response.json()
    
    # Récupération des valeurs de température actuelle et de température ressentie
    temp_actuelle = response_b['main']['temp']
    temp_ressentie = response_b['main']['feels_like']
    temp_min=response_b['main']['temp_min']
    temp_max= response_b['main']['temp_max']
    pression_atmo=['main']['pressure']
    humidité=['main']['humidity']
    vitesse_vent=['wind']['speed']
    dir_vent=['wind']['deg']
    lever_sol=['sys']['sunrise']
    coucher_sol=['sys']['sunset']
    
    # Ajout des valeurs au DataFrame sous forme d'une liste imbriquée
    df.loc[len(df)] = [i, temp_actuelle, temp_ressentie]

# Affichage du DataFrame mis à jour
print(df)