import pygame
import os

# Initialisation de Pygame
pygame.init()

# Définir les dimensions de la fenêtre (640x640) et les paramètres du bouton
window_size = (640, 720)  # 80 pixels supplémentaires pour le bouton
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Interface de dessin tactile")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREY = (200, 200, 200)

# Variables d'état
drawing = False
erasing = False
last_pos = None
line_thickness = 5  # Épaisseur du trait

# Remplir l'écran de blanc
screen.fill(WHITE)

# Créer une surface pour le bouton de sauvegarde
button_rect = pygame.Rect(220, 660, 200, 50)  # Rectangle du bouton (centré en bas)

# Fonction pour dessiner le bouton de sauvegarde
def draw_save_button():
    pygame.draw.rect(screen, GREY, button_rect)
    font = pygame.font.SysFont(None, 36)
    text = font.render("Sauvegarder", True, BLACK)
    screen.blit(text, (button_rect.x + 20, button_rect.y + 10))

# Fonction pour générer un nom de fichier unique
def generate_unique_filename():
    if not os.path.exists("images_gravures"):
        os.makedirs("images_gravures")
    
    # Générer un nom unique en utilisant l'horodatage
    return f"images_gravures/dessin_{pygame.time.get_ticks()}.png"

# Fonction pour nettoyer l'écran
def clear_screen():
    screen.fill(WHITE)  # Réinitialiser l'écran à blanc

# Boucle principale
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Début du dessin ou effacement
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                # Si on clique sur le bouton, sauvegarder l'image
                filename = generate_unique_filename()
                pygame.image.save(screen, filename)
                print(f"Image sauvegardée sous : {filename}")
                
                # Nettoyer l'écran après la sauvegarde
                clear_screen()
            else:
                drawing = True
                last_pos = pygame.mouse.get_pos()

        # Arrêter de dessiner ou d'effacer
        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

        # Changer le mode de dessin/effacement avec les touches
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                clear_screen()  # Réinitialiser l'écran
            if event.key == pygame.K_e:
                erasing = not erasing  # Activer ou désactiver la gomme

    # Si on dessine ou efface
    if drawing:
        mouse_pos = pygame.mouse.get_pos()
        if last_pos:
            color = WHITE if erasing else BLACK  # Si gomme activée, dessiner en blanc (effacement)
            pygame.draw.line(screen, color, last_pos, mouse_pos, line_thickness)
        last_pos = mouse_pos

    # Dessiner le bouton de sauvegarde
    draw_save_button()

    # Mettre à jour l'affichage
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
