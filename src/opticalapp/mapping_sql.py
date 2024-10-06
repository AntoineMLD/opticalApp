import sqlite3
import csv

# Connexion à la base de données SQLite
db_path = r'C:\Users\antoi\Documents\projet optique\prototype\src\opticalapp\engravings.db'
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Nom du fichier CSV à lire
input_csv = 'image_classes.csv'

# Insère les données dans la table engraving_classes
with open(input_csv, mode='r') as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        premiere_gravure = row['premiere_gravure']
        classes = row['Classes']

        try:
            # Vérifie si la gravure existe dans la table 'engravings' et récupère l'ID correspondant
            cur.execute("SELECT id FROM engravings WHERE premiere_gravure = ?", (premiere_gravure,))
            engraving = cur.fetchone()
            if engraving:
                engraving_id = engraving[0]
                # Insère la gravure avec toutes ses classes regroupées dans une seule entrée
                cur.execute("""
                    INSERT INTO engraving_classes (engraving_id, premiere_gravure, classe)
                    VALUES (?, ?, ?)
                """, (engraving_id, premiere_gravure, classes))
                print(f"Données insérées pour {premiere_gravure} (ID {engraving_id}) avec classes {classes}")
            else:
                print(f"Gravure {premiere_gravure} non trouvée dans la table engravings")
        except sqlite3.Error as e:
            print(f"Erreur lors de l'insertion : {e}")

# Valide les modifications et ferme la connexion
conn.commit()
cur.close()
conn.close()

print("Données insérées avec succès dans la table engraving_classes.")
