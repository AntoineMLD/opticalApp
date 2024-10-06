import os
from PIL import Image

# Chemin vers le dossier contenant les images
image_folder = "images_gravures"
output_folder = "images_gravures_640x640"  # Nouveau dossier pour les images redimensionnées

# Créer le dossier de sortie s'il n'existe pas
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Parcourir toutes les images dans le dossier
for filename in os.listdir(image_folder):
    if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".tif"):
        image_path = os.path.join(image_folder, filename)
        
        # Ouvrir l'image
        with Image.open(image_path) as img:
            # Redimensionner l'image à 640x640 pixels
            resized_img = img.resize((640, 640))
            
            # Enregistrer l'image redimensionnée dans le dossier de sortie
            resized_img.save(os.path.join(output_folder, filename))
            print(f"Image redimensionnée et enregistrée dans : {output_folder}/{filename}")

print("Toutes les images ont été redimensionnées.")
