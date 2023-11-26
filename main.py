import pygame
import sys
import random
from objects import *

# Initialisation de Pygame
pygame.init()

# Définir la taille de la fenêtre
largeur, hauteur = 800, 600
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Lancer de hamster")

# Couleur de fond
couleur_fond = (135, 206, 250)  # Bleu ciel

# Position initiale du hamster
hamster = Hamster(x=100, y=450, largeur=50, hauteur=50, vitesse_x=5, vitesse_y=-8)

elasticite = 5  # Élasticité du hamster lorsqu'il rebondit

# Score
score = 0

font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()  # Ajout de la clock

# Position initiale du décor
decor_x = 0

# Créer une liste d'obstacles (items)
obstacles = []

def creer_obstacle():
    # Choisir une classe d'item aléatoirement
    item_classe = random.choice([Fusée, Ventilateur, Balle, Tremplin])

    # Créer une instance de la classe d'item choisie avec des positions aléatoires
    return item_classe(
        x=hamster.x + largeur + random.randint(50, 200),
        y=random.randint(50, hauteur - 50),
        vitesse=2,  # Valeur arbitraire, à ajuster
    )

# Ajouter quelques obstacles au début
obstacles.append(creer_obstacle())

# Boucle de jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            hamster.vitesse_y -= elasticite

    # Mise à jour de la position du hamster en fonction de la vitesse
    hamster.deplacer()

    # Appliquer la gravité
    hamster.vitesse_y += 0.5  # Valeur arbitraire, à ajuster

    # Ajuster la position du décor en fonction du hamster
    decor_x += hamster.vitesse_x

    # Dessiner la couleur de fond
    fenetre.fill(couleur_fond)

    # Dessiner le hamster
    pygame.draw.rect(fenetre, (255, 69, 0), (hamster.x - decor_x, hamster.y, hamster.largeur, hamster.hauteur))

    # Dessiner les items
    for obstacle in obstacles:
        
        # Vérifier la collision
        if (
            hamster.x < obstacle.x + obstacle.largeur and
            hamster.x + hamster.largeur > obstacle.x and
            hamster.y < obstacle.y + obstacle.hauteur and
            hamster.y + hamster.hauteur > obstacle.y
        ):
            print("Collision avec un obstacle!")
            # Appeler la méthode utiliser de l'obstacle (l'item)
            obstacle.utiliser(hamster)
            
            # Supprimer l'obstacle de la liste
            obstacles.remove(obstacle)
            # Ajouter du score ou effectuer d'autres actions si nécessaire
            
    # Vérifier l'état de l'accélération de la fusée
    if hamster.acceleration_time > pygame.time.get_ticks() and hamster.vitesse_x < 15:
        # Si le temps d'accélération n'est pas écoulé, le hamster continue d'accélérer
        hamster.vitesse_x += 10
    else:
        # Si le temps est écoulé, réinitialiser la vitesse du hamster
        hamster.vitesse_x = 5  # Ajoutez la valeur correcte ici

    # Dessiner les items après avoir vérifié la collision
    for obstacle in obstacles:
        obstacle.dessiner(fenetre, decor_x)

    # Mettre à jour l'affichage
    pygame.display.flip()

    # Mettre à jour la position des obstacles (maintenant des items)
    obstacles = [obstacle for obstacle in obstacles if obstacle.x + obstacle.largeur > decor_x]

    # Ajouter de nouveaux obstacles (maintenant des items)
    if random.randint(0, 100) < 5:  # 5% de chance d'ajouter un nouvel obstacle
        obstacles.append(creer_obstacle())

    # Réguler le taux de rafraîchissement de l'écran
    clock.tick(30)  # 30 FPS (tu peux ajuster cette valeur en fonction de tes besoins)
