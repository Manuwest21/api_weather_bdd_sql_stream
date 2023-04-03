import requests
import datetime
import pandas as pd
boa=["toulouse","lille","bordeaux"]

# conversion : timestamp = 1680499203
# dt_object = datetime.datetime.fromtimestamp(timestamp)
# print("Heure de lever du soleil :", dt_object.time())


df = pd.DataFrame(columns=["ville" , "température actuelle" , "tempéreature ressentie", "température minimale", "température maximale", "pression atmosphérique", "humidité"])

url="https://api.openweathermap.org/data/2.5/weather"

params= {"q":"Gueugnon",
         "appid": "41a65c4b3f220173fa1f518a942388bc",
        "units": "metric"}

response = requests.get(url, params=params)


# print(response.json()['sys']['sunrise'])
print(response.json())

for i in boa:
    params={
        "q":i,
        "appid": "41a65c4b3f220173fa1f518a942388bc",
        "units": "metric"}
    response = requests.get(url, params=params)
    a=[]
    response_b=response.json()
    a.append(response_b['main']['temp'], response_b['main']['feels_like'])
    for d in a:
        df.loc[len(df)] = d