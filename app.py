import pandas as pd
import pymysql as maria


def lire_csv(nom_fichier: str):
    """permet de lire un fichier csv et le retourne en dataframe

    Args:
        nom_fichier (str): nom du fichier à lire exemple : clients.csv

    Returns:
        df: Dataframe contenant les données du fichier CSV
    """
    df=pd.read_csv(nom_fichier)
    print(df)
    return df

# table = lire_csv("clients.csv")

def se_connecter_db(host: str, user: str, password: str, database: str):
    """Permet de se connecter à la base de données.

    Args:
        host (str): Machine sur laquelle se trouve la base de données
        - localhost : si c'est sur la même machine   exemple : host
        - ip : si c'est sur une autre machine   exemple : 10.125.22.53
        user (str): nom d'utilisateur
        password (str): mot de pass de l'utilisateur
        database (str): nom de la base de données

    Returns:
        _type_: _description_
    """
    connexion = maria.connect(host=host, user=user, password=password, database=database)
    return connexion


db_host="localhost"
db_user="root"
db_password="example"
db_database="exercice"

#on se connecte à la base de données une connexion est un appel à la base de données.
con=se_connecter_db(db_host, db_user, db_password, db_database)

#un curseur ou pointeur qui va se placer sur la table.
curseur = con.cursor()

#On creer une requete sql pour ajouter les clients
#Je creer un template, un schéma
sql = "INSERT INTO clients (id, prenom, nom, email, profession, pays, ville) VALUES(%s, %s, %s, %s, %s, %s, %s)"



#On rempli le template avec les informations du csv
curseur.execute(sql, (7899, "Doe", "John", "john@test.fr", "pecheur", "France", "Lorient" ))

#On pousse les information
con.commit()

#On ferme la connexion
con.close()

#il suffira de lier ensuite le csv avec la requete à l'aide de python.