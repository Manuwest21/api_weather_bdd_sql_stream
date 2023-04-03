
import sqlite3

def creer_carnet_operations(temp_actu:float, temp_ressentie:float, temp_min:float, temp_max:float, pressure:int, humidité:int, vitesse_vent:float, dir_vent:str, lever_sol:str, coucher_sol:str) -> None:
    connexion = sqlite3.connect("bddeti.db")
    curseur = connexion.cursor()

    curseur.execute("""
                    INSERT INTO villes
                        VALUES ( ?, ?, ?, ?, ?,?,?,?,?,?)   
                    """, (temp_actu, temp_ressentie, temp_min, temp_max, pressure, humidité, vitesse_vent, dir_vent, lever_sol, coucher_sol))
    connexion.commit()

    connexion.close()