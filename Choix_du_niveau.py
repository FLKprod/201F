from regles.regles import regles
from jeu_cities import*
from jeu_countries import*

import pygame
import random
import math
import time
import os
from pygame.locals import*
import linecache

def choix_niveau():
    largeur, hauteur = 1000, 600
    white = (255, 255, 255)
    red = ( 255 , 100 , 100)
    couleur_texte = white
    font = pygame.font.SysFont("comicsansms", 50)


    pygame.init()
    fenetre = pygame.display.set_mode((1000, 600))
    fenetre.fill((69, 93, 215))

    text_ville = "Cherchez les villes !"
    text_ville_surface = font.render(text_ville, True, red)
    text_ville_rect = text_ville_surface.get_rect()
    text_ville_rect.center = (largeur // 4, hauteur // 5)

    text_France_ville = "France"
    text_France_ville_surface = font.render(text_France_ville, True, couleur_texte)
    text_France_ville_rect = text_France_ville_surface.get_rect()
    text_France_ville_rect.center = (largeur // 4, hauteur * 2 // 5)

    text_Europe_ville = "Europe"
    text_Europe_ville_surface = font.render(text_Europe_ville, True, couleur_texte)
    text_Europe_ville_rect = text_Europe_ville_surface.get_rect()
    text_Europe_ville_rect.center = (largeur // 4, hauteur * 3 // 5)

    text_Monde_ville = "Monde"
    text_Monde_ville_surface = font.render(text_Monde_ville, True, couleur_texte)
    text_Monde_ville_rect = text_Monde_ville_surface.get_rect()
    text_Monde_ville_rect.center = (largeur // 4, hauteur * 4 // 5)

    text_pays = "Cherchez les Pays !"
    text_pays_surface = font.render(text_pays, True, red)
    text_pays_rect = text_pays_surface.get_rect()
    text_pays_rect.center = (3 * largeur // 4, hauteur // 5)

    text_Europe_pays = "Europe"
    text_Europe_pays_surface = font.render(text_Europe_pays, True, couleur_texte)
    text_Europe_pays_rect = text_Europe_pays_surface.get_rect()
    text_Europe_pays_rect.center = (3 * largeur // 4, hauteur * 2 // 5)

    text_Monde_pays = "Monde"
    text_Monde_pays_surface = font.render(text_Monde_pays, True, couleur_texte)
    text_Monde_pays_rect = text_Monde_pays_surface.get_rect()
    text_Monde_pays_rect.center = (3 * largeur // 4, hauteur * 3 // 5)

    nom_image = "images/logo201F.png"
    chemin_image = os.path.join("", nom_image)
    image = pygame.image.load(chemin_image)
    image = pygame.transform.scale(image, (100, 100))
    fenetre.blit(image, (3 * largeur // 4 -50  , hauteur * 3 // 4))



    pygame.display.flip()
    boucle2 = True
    while boucle2 == True:
        fenetre.blit(text_ville_surface, text_ville_rect)
        fenetre.blit(text_France_ville_surface, text_France_ville_rect)
        fenetre.blit(text_Europe_ville_surface, text_Europe_ville_rect)
        fenetre.blit(text_Monde_ville_surface, text_Monde_ville_rect)
        fenetre.blit(text_pays_surface, text_pays_rect)
        fenetre.blit(text_Europe_pays_surface, text_Europe_pays_rect)
        fenetre.blit(text_Monde_pays_surface, text_Monde_pays_rect)

        for event in pygame.event.get():
            if event.type == QUIT:
                boucle2 = False
                choix_du_niveau = False
            elif event.type == KEYUP and event.key == K_ESCAPE:
                boucle2 = False
                choix_du_niveau = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                print("Clic de souris aux coordonnées :", x, y)
            
            if event.type == pygame.MOUSEMOTION:
                if text_France_ville_rect.collidepoint(event.pos):
                    couleur_texte = red
                else:
                    couleur_texte = white
                if text_Europe_ville_rect.collidepoint(event.pos):
                    couleur_texte = red
                else:
                    couleur_texte = white
                if text_Monde_ville_rect.collidepoint(event.pos):
                    couleur_texte = red
                else:
                    couleur_texte = white
                if text_Europe_pays_rect.collidepoint(event.pos):
                    couleur_texte = red
                else:
                    couleur_texte = white
                if text_Monde_pays_rect.collidepoint(event.pos):
                    couleur_texte = red
                else:
                    couleur_texte = white
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if text_France_ville_rect.collidepoint(event.pos):
                    regles("ville")
                    jeu_cities("france")
                    boucle2=False
                    choix_du_niveau=True
                elif text_Europe_ville_rect.collidepoint(event.pos):
                    regles("ville")
                    jeu_cities("europe")
                    boucle2=False
                    choix_du_niveau=True
                elif text_Monde_ville_rect.collidepoint(event.pos):
                    regles("ville")
                    jeu_cities("monde")
                    boucle2=False
                    choix_du_niveau=True
                elif text_Europe_pays_rect.collidepoint(event.pos):
                    regles("pays")
                    jeu_countries("europe")
                    boucle2=False
                    choix_du_niveau=True
                elif text_Monde_pays_rect.collidepoint(event.pos):
                    regles("pays")
                    jeu_countries("monde")
                    boucle2=False
                    choix_du_niveau=True
            else:
                pygame.display.flip()
                