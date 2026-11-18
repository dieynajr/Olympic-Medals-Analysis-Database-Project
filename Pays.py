import pandas as pd
import mysql.connector

# Lecture du fichier CSV
df = pd.read_csv("Olympicsmd.csv")

# Connexion MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="olympics_medals"
)

cursor = conn.cursor()

# Extraire les pays uniques
pays = df[['NOC']].drop_duplicates()

# Insertion dans la table Pays
for index, row in pays.iterrows():
    cursor.execute(
        "INSERT INTO Pays (NOC, Nom_Pays) VALUES (%s, %s)",
        (row['NOC'], row['NOC'])  # ici on met NOC comme nom si pas de dataset pays
    )

conn.commit()
cursor.close()
conn.close()

print("Table Pays alimentée avec succès")

# Récupérer les données
cursor.execute("SELECT NOC, Nb_Or FROM Palmares")

resultats = cursor.fetchall()

# Boucle + test
for ligne in resultats:
    noc = ligne[0]
    nb_or = ligne[1]
    
    if nb_or > 30:  # condition
        print(noc, "a beaucoup de médailles d'or :", nb_or)

cursor.close()
conn.close()

cursor.execute("DELETE FROM Palmares WHERE NOC = %s", ("France",))

conn.commit()  # obligatoire pour valider la suppression

print("Enregistrement supprimé")

cursor.close()
conn.close()

# Requête 1 : pays avec plus de 30 médailles d’or
cursor.execute("""
    SELECT NOC, Nb_Or
    FROM Palmares
    WHERE Nb_Or > 30
""")

resultat1 = cursor.fetchall()

print("Pays avec plus de 30 médailles d'or :")
for ligne in resultat1:
    print(ligne)


# Requête 2 : total des médailles d’or par pays
cursor.execute("""
    SELECT NOC, SUM(Nb_Or)
    FROM Palmares
    GROUP BY NOC
""")

resultat2 = cursor.fetchall()

print("\nTotal des médailles d'or par pays :")
for ligne in resultat2:
    print(ligne)


cursor.close()
conn.close()

annee = 2024
noc = "FRA"
rang = 1
nb_or = 10
nb_argent = 12
nb_bronze = 8

# Contrôles de saisie

if not isinstance(annee, int):
    print("Erreur : l'année doit être un entier")

elif len(noc) != 3:
    print("Erreur : le code NOC doit contenir 3 caractères")

elif nb_or < 0 or nb_argent < 0 or nb_bronze < 0:
    print("Erreur : les médailles ne peuvent pas être négatives")

elif rang is not None and rang < 0:
    print("Erreur : le rang doit être positif")

else:
    cursor.execute("""
        INSERT INTO Palmares (Annee, NOC, Rang, Nb_Or, Nb_Argent, Nb_Bronze)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (annee, noc, rang, nb_or, nb_argent, nb_bronze))

    conn.commit()
    print("Insertion réussie")

cursor.close()
conn.close()