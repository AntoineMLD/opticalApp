import os
import requests
import pandas as pd

# Charger le fichier CSV
df = pd.read_csv('test.csv')

# Créer un dossier pour enregistrer les images
output_folder = 'images_gravures'
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Fonction pour télécharger et sauvegarder une image
def download_image(url, output_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(output_path, 'wb') as f:
                f.write(response.content)
            print(f"Image téléchargée et enregistrée dans : {output_path}")
        else:
            print(f"Erreur lors du téléchargement de l'image : {url}")
    except Exception as e:
        print(f"Erreur : {e}")

# Boucle pour télécharger chaque image, en vérifiant les valeurs manquantes
for index, row in df.iterrows():
    image_url = row['premiere_gravure']  # Colonne contenant les chemins des images
    
    # Vérifier que l'URL est valide (pas NaN)
    if isinstance(image_url, str) and image_url.strip() != '':
        image_name = os.path.basename(image_url)  # Extraire le nom de l'image
        image_name = image_name.replace('web_', '')  # Enlever le préfixe 'web_'
        output_path = os.path.join(output_folder, image_name)  # Chemin de destination
        download_image(image_url, output_path)  # Télécharger l'image
    else:
        print(f"URL invalide pour l'entrée à l'index {index}")