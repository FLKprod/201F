import pygame, time, random, math, linecache
from pygame.locals import*
def jeu_countries(categorie):
    largeur, hauteur = 1000,600

    if categorie == "europe":
        carte=pygame.image.load("maps/PCarteEurope.png")
        xcarte, ycarte=21, 0
        xpays, ypays=40, 50 # texte de la ville
        xscore, yscore=40, 95 # affichage du texte pour le score
        xpoints, ypoints=130, 95 #affichage du score utilisateur
        xwin_or_loose, ywin_or_loose = 850, 10
        ycoeur = 15
        coeur_liste = [40, 80, 120, 160, 200]
    elif categorie == "monde":
        largeur = 1106
        light_blue = (200,200,255)
        carte=pygame.image.load("maps/PCarteMonde.png")
        xcarte, ycarte=0, 0
        xpays, ypays=300, 550 # texte de la ville
        xscore, yscore=890, 550 # affichage du texte pour le score
        xpoints, ypoints=970, 550 #affichage du score utilisateur
        xwin_or_loose, ywin_or_loose = 900 , 10
        ycoeur = 15
        coeur_liste = [15, 55, 95, 135, 175]
    fenetre = pygame.display.set_mode((largeur,hauteur))
    #couleurs utilisees
    white = (255,255,255)
    orange = (255,128,0)
    light_blue = (51, 189, 223)

    pygame.font.init()
    # Initialisation des textures
    correct_sound = pygame.mixer.Sound("sounds/correct.wav")
    fail_sound = pygame.mixer.Sound("sounds/fail.wav")
    error_sound = pygame.mixer.Sound("sounds/error.wav")

    coeur=pygame.image.load("Icones/coeur.png")
    ico_rouge=pygame.image.load("Icones/iconerouge.png")
    ico_noir = pygame.image.load("Icones/iconenoir.png")
    over = pygame.image.load("images/GameOver.jpg")
    win = pygame.image.load("images/win.png")
    lose = pygame.image.load("images/lose.png")


    # affichage des textures initiales
    chainescore="Score:"
    font = pygame.font.SysFont("comicsansms", 25)
    textscore=font.render(chainescore,1,white)
    points=0
    pygame.display.flip()
    continuer = True
    while continuer == True:
        # Affichage des premieres structures
        fenetre.fill(light_blue)
        fenetre.blit(carte,(xcarte,ycarte))
        fenetre.blit(coeur,(coeur_liste[0],ycoeur))
        fenetre.blit(coeur,(coeur_liste[1],ycoeur))
        fenetre.blit(coeur,(coeur_liste[2],ycoeur))
        fenetre.blit(coeur,(coeur_liste[3],ycoeur))
        fenetre.blit(coeur,(coeur_liste[4],ycoeur))
        # Affichages des structures d'affichage du score et de la distance
        textpoints=font.render(str(points),1,white)
        fenetre.blit(textscore,(xscore,yscore))
        fenetre.blit(textpoints,(xpoints,yscore))
        #Prise d'une ville au hasard et initialisation des variables nécésaire au déroulement d'un tour
        if categorie == "europe":
            names_file = "datas/PaysEurope.txt"
            cols_file = 'datas/ColPaysEurope.txt'
        elif categorie == "monde":
            names_file = "datas/PaysMonde.txt"
            cols_file = 'datas/ColPaysMonde.txt'
        
        fichier = open(names_file, 'r')
        NumberOfLine = 0
        for line in fichier:
            NumberOfLine += 1
        a = random.randint(1, NumberOfLine)
        b = a
        while a == b:
            a = random.randint(1, NumberOfLine)
        pays = linecache.getline(names_file, a).strip()
        fichierII = open(cols_file, 'r')
        colors = linecache.getline(cols_file, a)
        textpays = font.render(pays, 1, white)
        fenetre.blit(textpays, (xpays, ypays))
        red=int(colors[0]+colors[1]+colors[2])
        green = int(colors[4] + colors[5] + colors[6])
        blue = int(colors[8] + colors[9] + colors[10])
        couleurs=[red,green,blue]
        gagne=0
        vie=5
        pygame.display.flip()
        while gagne==0 and vie!=0:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button==1 :
                    position = event.pos
                    x=position[0]
                    y=position[1]-ycarte #ajout du decalage de la carte
                    colors=pygame.Surface.get_at(carte,(x,y))
                    couleurposition=[colors[0],colors[1],colors[2]]
                    #Choix de l'icone en fonction de la distance
                    if couleurs==couleurposition:
                        ico = ico_rouge
                        gagne = 1
                        points = points + 1
                        fenetre.blit(ico, (position[0] - 20, position[1] - 40))
                    else:
                        ico = ico_noir
                    fenetre.blit(carte,(xcarte,ycarte))
                    fenetre.blit(textscore,(xscore,yscore))
                    fenetre.blit(textpays, (xpays, ypays))
                    fenetre.blit(textpoints,(xpoints,yscore))
                    fenetre.blit(ico,(position[0]-20,position[1]-40))
                    pygame.display.flip()
                    vie = vie - 1
                    #Verification si succés

                    for vies_restante in range (0,vie):
                        fenetre.blit(coeur,(coeur_liste[vies_restante],ycoeur))
                    if vie==0 and gagne!=1 :
                        lose = pygame.transform.scale(lose, (100, 100))
                        fenetre.blit(lose, (xwin_or_loose, ywin_or_loose))
                        pygame.display.flip()
                        error_sound.play()
                        pygame.time.wait(int(error_sound.get_length()) * 1000)
                        k=i=j=0
                        for k in range(0,4):
                            for i in range(0,979):
                                for j in range(0,600):
                                    colorpixel = pygame.Surface.get_at(carte,(i, j))
                                    cpixel=[colorpixel[0],colorpixel[1],colorpixel[2]]
                                    if couleurs==cpixel:
                                        pygame.Surface.set_at(carte,(i, j),(0,255,0))
                                    j+=1
                                i+=1
                            time.sleep(0.01)
                            
                            fenetre.blit(carte, (xcarte, ycarte))
                            fenetre.blit(textscore,(xscore,yscore))
                            fenetre.blit(textpays, (xpays, ypays))
                            fenetre.blit(textpoints,(xpoints,yscore))
                            pygame.display.flip()
                            i=j=0
                            for i in range(0,979):
                                for j in range(0,600):
                                    colorpixel = pygame.Surface.get_at(carte,(i, j))
                                    cpixel=[colorpixel[0],colorpixel[1],colorpixel[2]]
                                    if cpixel==[0,255,0]:
                                        pygame.Surface.set_at(carte, (i, j), (couleurs))
                                    j+=1
                                i+=1
                            time.sleep(0.1)
                            
                            fenetre.blit(carte, (xcarte, ycarte))
                            fenetre.blit(textscore,(xscore,yscore))
                            fenetre.blit(textpays, (xpays, ypays))
                            fenetre.blit(textpoints,(xpoints,yscore))
                            pygame.display.flip()
                            k+=1
                        fenetre.blit(carte, (xcarte, ycarte))
                        fenetre.blit(textscore,(xscore,yscore))
                        fenetre.blit(textpays, (xpays, ypays))
                        fenetre.blit(textpoints,(xpoints,yscore))
                        pygame.display.flip()
                        continuer = False
                    if gagne==1:
                        win = pygame.transform.scale(win, (100, 100))
                        fenetre.blit(win, (xwin_or_loose, ywin_or_loose))
                        pygame.display.flip()
                        correct_sound.play()
                        pygame.time.wait(int(correct_sound.get_length() * 1000))
                    pygame.display.flip()
                if event.type == QUIT:
                    gagne=1
                    continuer = False
                elif event.type == KEYUP and event.key == K_ESCAPE:
                    gagne=1
                    continuer = False
    fenetre.fill(white)
    image = pygame.transform.scale(over, (1000, 600))
    fenetre.blit(over, (0, 0))
    pygame.display.flip()
    fail_sound.play()
    pygame.time.wait(int(fail_sound.get_length() * 1000))
    pygame.display.flip()