import sqlite3
import os

class CsvPipeline:
    def process_item(self, item, spider):
        # Ici, l'URL complète reste intacte dans le CSV
        return item


class DataCleaningPipeline:

    def process_item(self, item, spider):
        # Nettoyage des données
        item['indice'] = None if item['indice'] == "Indice non disponible" else item['indice']
        item['matiere'] = None if item['matiere'] == "Matière non disponible" else item['matiere']

        # Conserver l'URL complète sans modifier premiere_gravure
        return item


class DatabasePipeline:

    def open_spider(self, spider):
        # Connexion à la base de données
        self.connection = sqlite3.connect("engravings.db")
        self.cursor = self.connection.cursor()

        # Créer la table si elle n'existe pas encore
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS engravings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom_gravure TEXT,
                indice TEXT,
                matiere TEXT,
                haut_de_montage TEXT,
                fournisseur TEXT,
                premiere_gravure TEXT
            )
        ''')

    def close_spider(self, spider):
        # Fermer la connexion à la base de données
        self.connection.commit()
        self.connection.close()

    def process_item(self, item, spider):
        # Garder l'URL complète intacte pour d'autres usages comme le CSV
        url_complète = item.get('premiere_gravure')
        
        # Modifier uniquement le nom du fichier, en enlevant 'web_' pour l'enregistrement dans la base
        if url_complète:
            nom_image = os.path.basename(url_complète)
            nom_image_modifié = nom_image.replace('web_', '')
            item_modifié = item.copy()
            item_modifié['premiere_gravure'] = nom_image_modifié  # Nom modifié uniquement pour la base de données

            # Insertion des données dans la base de données
            self.cursor.execute('''
                INSERT INTO engravings (nom_gravure, indice, matiere, haut_de_montage, fournisseur, premiere_gravure)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                item_modifié.get('nom_gravure'),
                item_modifié.get('indice'),
                item_modifié.get('matiere'),
                item_modifié.get('haut_de_montage'),
                item_modifié.get('fournisseur'),
                item_modifié.get('premiere_gravure')  # Nom de fichier modifié
            ))
        
        return item