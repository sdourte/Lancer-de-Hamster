import pygame
import random
import time

class Hamster:
    def __init__(self, x, y, largeur, hauteur, vitesse_x, vitesse_y, balle):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.vitesse_x = vitesse_x
        self.vitesse_y = vitesse_y
        self.balle = balle
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
        pygame.draw.rect(fenetre, (169,169,169), (self.x - decor_x, self.y, self.largeur, self.hauteur))

class Balle(Item):
    def __init__(self, x, y, vitesse, couleur):
        super().__init__(x, y, vitesse, largeur=20)
        # Propriétés spécifiques à la balle
        self.couleur = couleur
        
    def utiliser(self, hamster):
        print("On récolte une balle")

    def rebondir(self, hamster, couleur):
        # Méthode spécifique à la balle
        print("On utilise une balle")
        # On fait une condition pour gérer le cas où la vitesse n'est pas très grande mais faut quand même que ça rebondisse
        if hamster.vitesse_y <= 20:
            if couleur == "rose":
                hamster.vitesse_y = -15
            elif couleur == "jaune":
                hamster.vitesse_y = -30
        else:
            # Ici on part du principe que plus on tombe de haut, plus on va rebondir
            if couleur == "rose":
                hamster.vitesse_y = -hamster.vitesse_y * 1.2
            elif couleur == "jaune":
                hamster.vitesse_y = -hamster.vitesse_y * 1.4
        #hamster.vitesse_y -= rebond

    def dessiner(self, fenetre, decor_x):
        # Méthode pour dessiner la balle
        if self.couleur == "rose":
            pygame.draw.circle(fenetre, (255,20,147), (int(self.x - decor_x), int(self.y)), self.largeur)
        if self.couleur == "jaune":
            pygame.draw.circle(fenetre, (255, 255, 0), (int(self.x - decor_x), int(self.y)), self.largeur)

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
        pygame.draw.rect(fenetre, (139,69,19), (self.x - decor_x, self.y, self.largeur, self.hauteur))

class Skate():
    pass