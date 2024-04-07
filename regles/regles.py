import pygame, random, math
from pygame.locals import*
def regles(categorie):
   fenetre = pygame.display.set_mode((1000, 600))
   fenetre.fill((57, 234, 250))
   if categorie == "pays":
      regle=pygame.image.load("regles/Pregle.PNG")
   elif categorie == "ville":
      regle=pygame.image.load("regles/regle.png")
   fenetre.blit(regle,(0,0))
   pygame.display.flip()
   continuer = True
   while continuer == True:
      for event in pygame.event.get():
            if event.type == KEYUP and event.key == K_ESCAPE:
               continuer=False
            if event.type == KEYUP and event.key == K_RETURN:
               continuer=False
               pygame.display.flip()
            if event.type == QUIT:
               continuer = False