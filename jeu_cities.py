import pygame, random, math, time,linecache
from pygame.locals import*

def jeu_cities(categorie):
    largeur, hauteur = 1000,600

    #couleurs utilisees
    white = (255,255,255)
    orange = (255,128,0)
    blue = (100,100,255)


    if categorie == "france":
        carte=pygame.image.load("maps/CarteFrance.jpg")
        xcarte, ycarte=0, 0
        xville, yville=610, 70 # texte de la ville
        xecart, yecart = 740, 140 # affichage de la distance
        xdistance, ydistance = 610, 140 # texte pour la distance
        xscore, yscore=610, 210 # affichage du texte pour le score
        xpoints, ypoints=700, 210 #affichage du score utilisateur
        xwin_or_loose, ywin_or_loose = 610 , 280
        ycoeur = 15
        coeur_liste = [615, 655, 695, 735, 775]
    elif categorie == "europe":
        carte=pygame.image.load("maps/CarteEurope.png")
        xcarte, ycarte=0, 0
        xville, yville=15, 140 # texte de la ville
        xecart, yecart = 145, 50 # affichage de la distance
        xdistance, ydistance = 15, 50 # texte pour la distance
        xscore, yscore=15, 95 # affichage du texte pour le score
        xpoints, ypoints=110, 95 #affichage du score utilisateur
        xwin_or_loose, ywin_or_loose = 850, 10
        ycoeur = 15
        coeur_liste = [15, 55, 95, 135, 175]
    elif categorie == "monde":
        largeur = 1106
        blue = (200,200,255)
        carte=pygame.image.load("maps/CarteMonde.png")
        xcarte, ycarte=0, 0
        xville, yville=300, 550 # texte de la ville
        xecart, yecart = 750, 550 # affichage de la distance
        xdistance, ydistance = 610, 550 # texte pour la distance
        xscore, yscore=890, 550 # affichage du texte pour le score
        xpoints, ypoints=970, 550 #affichage du score utilisateur
        xwin_or_loose, ywin_or_loose = 710 , 400
        ycoeur = 15
        coeur_liste = [15, 55, 95, 135, 175]
    fenetre = pygame.display.set_mode((largeur,hauteur))

    # Initialisation des textures et des sons du jeu
    correct_sound = pygame.mixer.Sound("sounds/correct.wav")
    fail_sound = pygame.mixer.Sound("sounds/fail.wav")
    error_sound = pygame.mixer.Sound("sounds/error.wav")

    coeur=pygame.image.load("Icones/coeur.png")
    ico_bleu=pygame.image.load("Icones/iconebleu.png")
    ico_jaune=pygame.image.load("Icones/iconejaune.png")
    ico_vert=pygame.image.load("Icones/iconevert.png")
    ico_orange=pygame.image.load("Icones/iconeorange.png")
    ico_rouge=pygame.image.load("Icones/iconerouge.png")
    ico_noir = pygame.image.load("Icones/iconenoir.png")

    over = pygame.image.load("images/GameOver.jpg")
    win = pygame.image.load("images/win.png")
    lose = pygame.image.load("images/lose.png")

    
    # affichage des textures initiales
    chainescore="Score:"
    font = pygame.font.SysFont("comicsansms", 25)
    textscore=font.render(chainescore,1,orange)
    points=0
    chainedistance = "Distance = ____ km"
    textdistance = font.render(chainedistance, 1, blue)
    fenetre.blit(textdistance, (xdistance, ydistance))

    pygame.display.flip()
    continuer = True
    while continuer == True:
        # Affichage des premieres structures
        fenetre.fill(white)
        fenetre.blit(carte,(xcarte,ycarte))
        fenetre.blit(coeur,(coeur_liste[0],ycoeur))
        fenetre.blit(coeur,(coeur_liste[1],ycoeur))
        fenetre.blit(coeur,(coeur_liste[2],ycoeur))
        fenetre.blit(coeur,(coeur_liste[3],ycoeur))
        fenetre.blit(coeur,(coeur_liste[4],ycoeur))

        # Affichages des structures d'affichage du score et de la distance
        textpoints=font.render(str(points),1,orange)
        fenetre.blit(textscore,(xscore,yscore))
        fenetre.blit(textpoints,(xpoints,ypoints))
        fenetre.blit(textdistance,(xdistance, ydistance))
        textdistance = font.render(chainedistance, 1, blue)
        fenetre.blit(textdistance, (xdistance, ydistance))

        #Prise d'une ville au hasard et initialisation des variables nécésaire au déroulement d'un tour
        if categorie == "france":
            names_file = "datas/villesfrance.txt"
            coors_file = 'datas/coorfrance.txt'
        elif categorie == "europe":
            names_file = "datas/villeseurope.txt"
            coors_file = 'datas/cooreurope.txt'
        elif categorie == "monde":
            names_file = "datas/villesmonde.txt"
            coors_file = 'datas/coormonde.txt'
        fichier = open(names_file, 'r')
        NumberOfLine = 0
        for line in fichier:
            NumberOfLine += 1
        a=random.randint(1,NumberOfLine)
        b = a
        while a==b:
            a = random.randint(1,NumberOfLine)
        v = linecache.getline(names_file, a).strip()
        fichierII = open(coors_file, 'r')
        xy = linecache.getline(coors_file, a)
        textville = font.render(v, 1, blue)
        fenetre.blit(textville, (xville, yville))
        X=int(xy[0]+xy[1]+xy[2])
        Y=int(xy[4]+xy[5]+xy[6])
        ville=[X,Y]
        gagne=0
        vie=5
        pygame.display.flip()

        while gagne==0 and vie!=0:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN and event.button==1 :
                    position=event.pos
                    x = abs(ville[0] - position[0])
                    y = abs(ville[1] - (position[1]))
                    distance=int(math.sqrt((x-xcarte)**2+(y-ycarte)**2))
                    if categorie == "france":
                        ecart = int(distance * 2)
                    elif categorie == "europe":
                        ecart = int(distance * 900 / 178)
                    elif categorie == "monde":
                        ecart = int (distance * 22000 / 1106 )
                        print(ecart)
                
                    #Calcul et affichage de la distance
                    textdistance = font.render(chainedistance, 1, blue)
                    fenetre.blit(textdistance, (xdistance, ydistance))
                   
                    textecart = font.render(str(ecart), 1, blue)

                    #Choix de l'icone en fonction de la distance
                    if distance>=100:
                        ico=ico_bleu
                    elif distance<100 and distance>=72:
                         ico=ico_vert
                    elif distance<72 and distance>=41:
                        ico=ico_jaune
                    elif distance<41 and distance>=20:
                        ico=ico_orange
                    elif distance<20 :
                        ico=ico_rouge
                        gagne=1
                        points=points+1
                        fenetre.blit(carte,(xcarte,ycarte))
                        fenetre.blit(ico,(position[0]-20,position[1]-40))

                    # Affichage des textures apres modifications
                    fenetre.fill((255, 255, 255))
                    fenetre.blit(carte,(xcarte,ycarte))
                    fenetre.blit(textecart, (xecart, yecart))
                    fenetre.blit(textscore,(xscore,yscore))
                    fenetre.blit(textville,(xville,yville))
                    fenetre.blit(textpoints,(xpoints,ypoints))
                    fenetre.blit(textdistance, (xdistance, ydistance))
                    fenetre.blit(ico,(position[0]-20,position[1]-40))

                    vie = vie - 1

                    #Verification si succés
                    for vies_restante in range (0,vie):
                        fenetre.blit(coeur,(coeur_liste[vies_restante],ycoeur))
                    if vie==0 and gagne!=1 :
                        fenetre.blit(ico_noir, (ville[0]+xcarte-20,ville[1]+ycarte-40))
                        pygame.draw.circle(fenetre,(40,40,40),(ville[0]+xcarte,ville[1]+ycarte),distance,1)
                        lose = pygame.transform.scale(lose, (100, 100))
                        fenetre.blit(lose, (xwin_or_loose, ywin_or_loose))
                        pygame.display.flip()
                        error_sound.play()
                        pygame.time.wait(2000)
                        
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
    fenetre.fill((255, 255, 255))
    over = pygame.transform.scale(over, (1000, 600))
    fenetre.blit(over, (0, 0))
    pygame.display.flip()
    fail_sound.play()
    pygame.time.wait(int(fail_sound.get_length() * 1000))
    pygame.display.flip()