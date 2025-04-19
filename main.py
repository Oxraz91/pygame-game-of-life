import pygame
from math import *
from random import *

pygame.init()
RES = 30
LARGEUR, HAUTEUR = 1200, 900
noir = (10,9,17)
blanc = (255,255,255,0.1)
b = (52,52,52)
class Game:
    def __init__(self, largeur, hauteur, resolution):
        self.largeur = largeur
        self.hauteur = hauteur
        self.resolution = resolution
        self.screen = pygame.display.set_mode((self.largeur, self.hauteur))
        pygame.display.set_caption("Le Jeu de la vie de John Conway")
        self.nb_colonne = self.largeur // resolution
        self.nb_ligne = self.hauteur // resolution
        self.grille = self.tableau2d()

    def tableau2d(self):
        liste = [0] * self.nb_colonne
        for i in range(len(liste)):
            liste[i] = [0] * self.nb_ligne
        return liste

    def init_grille(self):
        for i in range(self.nb_colonne):
            for j in range(self.nb_ligne):
                self.grille[i][j] = floor(2*random())
        return self.grille

    def quadrillage(self):
        for i in range(0,self.hauteur,self.resolution):
            pygame.draw.line(self.screen,b,(0,i),(self.largeur,i))
        for i in range(0,self.largeur,self.resolution):
            pygame.draw.line(self.screen,b,(i,0),(i,self.hauteur))

    def compte_voisin(self, x, y):
        s = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                colonne = (x + i + self.nb_colonne) % self.nb_colonne
                ligne = (y + j + self.nb_ligne) % self.nb_ligne
                s += self.grille[colonne][ligne]
        s -= self.grille[x][y]
        return s

    def maj_voisin(self):
        nv_grille = self.tableau2d()
        for i in range(self.nb_colonne):
            for j in range(self.nb_ligne):
                s = 0
                voisin = self.compte_voisin(i, j)
                etat = self.grille[i][j]
                if etat == 0 and voisin == 3:
                    nv_grille[i][j] = 1
                elif etat == 1 and (voisin < 2 or voisin > 3):
                    nv_grille[i][j] = 0
                else:
                    nv_grille[i][j] = etat

        self.grille = nv_grille

    def dessin_grille(self):
        for i in range(self.nb_colonne):
            for j in range(self.nb_ligne):
                x = i * RES
                y = j * RES
                if self.grille[i][j] == 1:
                    Rectangle = pygame.Rect(x, y,RES,RES)
                    Rectangle.inflate_ip(-3,-3)
                    pygame.draw.rect(self.screen, blanc, Rectangle)

run = True
FPS = 10
jeu = Game(LARGEUR, HAUTEUR, RES)
jeu.grille = jeu.init_grille()
clock = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    jeu.screen.fill(noir)
    jeu.dessin_grille()
    #jeu.quadrillage()
    jeu.maj_voisin()
    pygame.display.update()
    clock.tick(FPS)

