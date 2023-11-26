import pygame
import random
import time

class Hamster:
    def __init__(self, x, y, largeur, hauteur, vitesse_x, vitesse_y):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.vitesse_x = vitesse_x
        self.vitesse_y = vitesse_y
        self.acceleration_time = 0

    def deplacer(self):
        # Méthode pour mettre à jour la position en fonction de la vitesse
        self.x += self.vitesse_x
        self.y += self.vitesse_y

class Item:
    def __init__(self, x, y, vitesse, largeur=20, hauteur=20):
        self.x = x
        self.y = y
        self.vitesse = vitesse
        self.largeur = largeur
        self.hauteur = hauteur
        # Ajoute d'autres propriétés communes à tous les items si nécessaire

    def utiliser(self):
        # Méthode appelée lorsque le hamster utilise l'item
        pass

    def dessiner(self, fenetre, decor_x):
        # Méthode pour dessiner l'item
        pass

class Fusée(Item):
    def __init__(self, x, y, vitesse):
        super().__init__(x, y, vitesse, largeur=20, hauteur=40)
        # Propriétés spécifiques à la fusée
        self.activation_time = 0

    def utiliser(self, hamster):
        print("Activation d'une fusée")
        hamster.acceleration_time = pygame.time.get_ticks() + 2000  # Accélère pendant 2000 millisecondes (2 secondes)

    def dessiner(self, fenetre, decor_x):
        # Méthode pour dessiner la fusée
        pygame.draw.rect(fenetre, (255, 0, 0), (self.x - decor_x, self.y, self.largeur, self.hauteur))

class Ventilateur(Item):
    def __init__(self, x, y, vitesse):
        super().__init__(x, y, vitesse, largeur=20, hauteur=40)
        # Propriétés spécifiques au ventilateur

    def utiliser(self, hamster):
        # Méthode spécifique au ventilateur
        print("Activation d'un ventilo")
        hamster.vitesse_y -= 20

    def dessiner(self, fenetre, decor_x):
        # Méthode pour dessiner le ventilateur
        pygame.draw.rect(fenetre, (0, 255, 0), (self.x - decor_x, self.y, self.largeur, self.hauteur))

class Balle(Item):
    def __init__(self, x, y, vitesse):
        super().__init__(x, y, vitesse, largeur=20)
        # Propriétés spécifiques à la balle

    def utiliser(self, hamster):
        # Méthode spécifique à la balle
        print("On récolte une balle")

    def dessiner(self, fenetre, decor_x):
        # Méthode pour dessiner la balle
        pygame.draw.circle(fenetre, (0, 0, 255), (int(self.x - decor_x), int(self.y)), self.largeur)

class Tremplin(Item):
    def __init__(self, x, y, vitesse):
        super().__init__(x, y, vitesse, largeur=20, hauteur=40)
        # Propriétés spécifiques au tremplin

    def utiliser(self, hamster):
        # Méthode spécifique au tremplin
        print("Activation d'un tremplin")
        hamster.acceleration_time = pygame.time.get_ticks() + 2000
        hamster.vitesse_y -= 30  # Ajustez cette valeur en fonction de la force désirée

    def dessiner(self, fenetre, decor_x):
        # Méthode pour dessiner le tremplin
        pygame.draw.rect(fenetre, (0, 0, 255), (self.x - decor_x, self.y, self.largeur, self.hauteur))

class Skate():
    pass