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
hamster = Hamster(x=100, y=450, largeur=50, hauteur=50, vitesse_x=0, vitesse_y=0)  # Vitesse initialisée à 0

# Vitesse initiale lorsque la partie démarre (ajoutée)
vitesse_initiale = -10

elasticite = 5  # Élasticité du hamster lorsqu'il rebondit

# Score
score = 0

font = pygame.font.Font(None, 36)

clock = pygame.time.Clock()  # Ajout de la clock

# Position initiale du décor
decor_x = 0

# Créer une liste d'obstacles (items)
obstacles = []

# État de la partie (pause au début)
en_partie = False

def creer_obstacle():
    # Choisir une classe d'item aléatoirement
    item_classe = random.choice([Fusée, Ventilateur, Balle, Tremplin])

    if item_classe == Tremplin:
        # Si c'est un tremplin, assurez-vous qu'il apparaît seulement sur le sol
        return item_classe(
            x=hamster.x + largeur + random.randint(50, 200),
            y=hauteur - 40,  # Ajustez cette valeur pour le placer sur le sol
            vitesse=2,  # Valeur arbitraire, à ajuster
        )
    else:
        # Sinon, créez l'obstacle normalement avec des positions aléatoires
        return item_classe(
            x=hamster.x + largeur + random.randint(50, 200),
            y=random.randint(50, hauteur - 50),
            vitesse=2,  # Valeur arbitraire, à ajuster
        )
        
# Nouvelles variables pour le décrément progressif du décor
temps_dernier_hamster = pygame.time.get_ticks()

# Boucle de jeu
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Gestion de la touche espace pour démarrer la partie
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            en_partie = True
            # Ajout de la vitesse initiale lorsque la partie démarre
            hamster.vitesse_y = vitesse_initiale

        if en_partie:  # Ajouter cette condition pour ignorer les événements si la partie est en pause
            if event.type == pygame.MOUSEBUTTONDOWN:
                hamster.vitesse_y -= elasticite  # Attention ici peut causer problème

    if en_partie:  # Ajouter cette condition pour ignorer la mise à jour du hamster si la partie est en pause
        # Mise à jour de la position du hamster en fonction de la vitesse
        hamster.deplacer()

        # Appliquer la gravité
        hamster.vitesse_y += 0.5  # Valeur arbitraire, à ajuster

        # Si le hamster est au sol, ajuster son comportement
        if hamster.y >= hauteur - hamster.hauteur:
            hamster.y = hauteur - hamster.hauteur  # Ajuster la position au sol
            hamster.vitesse_y = -hamster.vitesse_y * 0.5  # Rebondir avec une élasticité réduite
            print(hamster.vitesse_x, decor_x)

            # Si la vitesse en x est très faible, le hamster s'arrête complètement
            # On vérifie la vitesse y du hamster pour voir quand il ne rebondit plus
            if hamster.vitesse_y > -1:
                
                # On fait glisser le hamster
                hamster.vitesse_y = 0

                # Ici, vous pouvez ajouter la logique pour lancer le hamster suivant
                # Réinitialiser la position initiale, la vitesse, etc.
                hamster.x = 100
                hamster.y = 450
                hamster.vitesse_x = 0  # Mise à 0 pour s'assurer que le hamster est complètement arrêté
                hamster.vitesse_y = 0  # Ajuster à 0 pour éviter que le hamster ne tombe automatiquement

                # Ajouter des points en fonction de la distance parcourue
                score += int(hamster.x - decor_x)

                # Revenir en arrière dans le décor
                #decor_x = 0  # Ajustez la valeur 200 en fonction de vos besoins
                
                # On stoppe le hamster
                en_partie = False

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
            if obstacle.__class__ != Tremplin:
                obstacles.remove(obstacle)
            # Ajouter du score ou effectuer d'autres actions si nécessaire
            
    # Vérifications pour faire le retour en arrière
    if hamster.vitesse_y == 0 and decor_x != 0 and not en_partie:
        decor_x -= 20
    # Si jamais le decor_x n'est pas modulo 20
    if decor_x < 0:
        decor_x = 0

    # Vérifier l'état de l'accélération de la fusée
    if en_partie and hamster.acceleration_time > pygame.time.get_ticks() and hamster.vitesse_x < 15:
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
    if en_partie and random.randint(0, 100) < 5:  # 5% de chance d'ajouter un nouvel obstacle
        obstacles.append(creer_obstacle())

    # Réguler le taux de rafraîchissement de l'écran
    clock.tick(30)  # 30 FPS (tu peux ajuster cette valeur en fonction de tes besoins)
