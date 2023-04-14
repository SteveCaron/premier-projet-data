import pandas as p
import datetime

file_path = "clients.csv"
data_frame = p.read_csv(file_path)

# La méthode head affiche les premières valeurs du tableau, 5 par defaut
# Pandas comprend que la première ligne est un header. Et supprime les lignes vides au dessus.
print(data_frame.head())

# Affiche les infos de la dataFrame
print(data_frame.info())

# Comptre le nombre de professions et leurs occurences.
professions = data_frame["profession"].value_counts()
print(professions)

# Affiche les 10 premieres lignes, dont le lastname commence par la lettre D
# Il faut cast la colonne lastname en string pour pouvoir utiliser la méthode startwith.
# De base "lastname" est de type objet, cc .info()
gensD = data_frame[data_frame["lastname"].str.startswith("D")].head(10)
print(gensD)

# Selectionner des colonnes d'un premier tableau et les mettre dans un deuxième.
# On met deux crochets car il y a plus de une colonne. C'est comme une parenthèse
contact = data_frame[["firstname", "lastname", "email"]]
print(contact.head())

# Trie les données selon la colonne lastname
sorted_data = contact.sort_values(by="lastname")
print(sorted_data)

# Transfert mon dataFrame vers un fichier csv
sorted_data.to_csv("clients_tries.csv")


# Mode retourn la/les valeurs la plus commune
# mode() retourne un dataFrame car je l'utilise sur un dataframe
# iloc[] permet d'afficher la position 0 du dataFrame
villes_communes = data_frame["city"].mode().iloc[0]
print(f"La ville la plus fréquente est : {villes_communes}")


# Extrait les lignes de ma dataFrame dont la proffesion est developper
data_scientist = data_frame[data_frame["profession"] == "developer"]
print(data_scientist)


# je cast la colonne "Birthdate" au format date, en précisant le format de la date (m-d-Y).
# Il réorganise la date dans le nouveau df au format américain.
data_frame["birthdate"] = p.to_datetime(
    data_frame["birthdate"], format="%m-%d-%Y")


def calcul_age(birthdate):

    # Enregistre dans la varible today, la date d'aujourd'hui
    today = datetime.datetime.now()
    # Calcul l'age de la personne, = son nombre d'année.
    # Si la personne n'as pas feter son anniversire, il faut lui retirer 1 an.
    # On fait alors la comparaison : sa date d'anniversaire est plus grande que la date d'aujourd'hui (il n'a pas feter son anniversaire cette année) -> renvoie un booléen True
    # Un booléen True à une valeur de 1 & Un booléen False à une valeur de 0
    # Si il n'a pas feter son anniversaire en faisant  "Age - True" on fait en réalité "Age - 1" On ajuste donc son age
    age = today.year - birthdate.year - \
        ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


# Creer la colone "age" et la remplis en appliquant la fonction calcul_age à la colonne "birthdate"
data_frame["age"] = data_frame["birthdate"].apply(calcul_age)


print(data_frame[["birthdate", "age"]])

# je regroupe mes profession ensemble et j'affecte la moyenne de l'age pour chaque profession
age_par_profession = data_frame.groupby("profession")["age"].mean()
print(age_par_profession)

salaire_par_profession = data_frame.groupby('profession')["salary"].mean()
print(salaire_par_profession)




#afficher les lignes de mon df qui on un salaire > 5000 
high_salary = data_frame[data_frame["salary"] > 5000]
print(high_salary)


#Compte le nombre d'occurence de pays, et le normalise sur le nombre total de ligne (occurence de pays / nombre total d'enregistrement)
# *100 pour avoir un pourcentage.
pourcentage_par_pays = data_frame["country"].value_counts(normalize=True) *100
print(pourcentage_par_pays)

#Affiche le salaire minimum
salaire_minimum = data_frame["salary"].min()
print (f"Le salaire minimum est de {salaire_minimum}")


salaire_minimum_par_pays = data_frame.groupby("country")["salary"].min().sort_values()
print(salaire_minimum_par_pays)
salaire_maximum_par_pays = data_frame.groupby('country')["salary"].max().sort_values(ascending=False)
print(salaire_maximum_par_pays)
salaire_moyen_par_pays = data_frame.groupby("country")["salary"].mean().sort_index(ascending=True)
print(salaire_moyen_par_pays)

age_filtre = data_frame[data_frame["age"]==30]
print(age_filtre)

print ("----------------------------------------------")



# #Passer la date au format jour-mois-date
# data_frame_date=data_frame["birthdate"].dt.strftime("%d\%m\%Y")
# print(data_frame_date)
# max_salary_by_country = data.groupby('country')['salary'].max()