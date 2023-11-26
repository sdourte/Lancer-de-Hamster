import pygame
import random

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

    def utiliser(self):
        # Méthode spécifique à la fusée
        pass

    def dessiner(self, fenetre, decor_x):
        # Méthode pour dessiner la fusée
        pygame.draw.rect(fenetre, (255, 0, 0), (self.x - decor_x, self.y, self.largeur, self.hauteur))

class Ventilateur(Item):
    def __init__(self, x, y, vitesse):
        super().__init__(x, y, vitesse, largeur=20, hauteur=40)
        # Propriétés spécifiques au ventilateur

    def utiliser(self):
        # Méthode spécifique au ventilateur
        pass

    def dessiner(self, fenetre, decor_x):
        # Méthode pour dessiner le ventilateur
        pygame.draw.rect(fenetre, (0, 255, 0), (self.x - decor_x, self.y, self.largeur, self.hauteur))

class Balle(Item):
    def __init__(self, x, y, vitesse):
        super().__init__(x, y, vitesse, largeur=20)
        # Propriétés spécifiques à la balle

    def utiliser(self):
        # Méthode spécifique à la balle
        pass

    def dessiner(self, fenetre, decor_x):
        # Méthode pour dessiner la balle
        pygame.draw.circle(fenetre, (0, 0, 255), (int(self.x - decor_x), int(self.y)), self.largeur)

class Tremplin(Item):
    def __init__(self, x, y, vitesse):
        super().__init__(x, y, vitesse, largeur=20, hauteur=40)
        # Propriétés spécifiques au tremplin

    def utiliser(self):
        # Méthode spécifique au tremplin
        pass

    def dessiner(self, fenetre, decor_x):
        # Méthode pour dessiner le tremplin
        pygame.draw.rect(fenetre, (0, 0, 255), (self.x - decor_x, self.y, self.largeur, self.hauteur))
