from Choix_du_niveau import*
import pkgutil
import subprocess
import os

if not pkgutil.find_loader('pygame'):
    print("Pygame n'est pas installé. Installation en cours...")
    subprocess.check_call(['pip', 'install', 'pygame'])
    print("Pygame a été installé avec succès.")
else:
    print("Pygame est déjà installé.")

intro=True
r=g=b=i=0
menu=True
while menu:
    choix_du_niveau=False
    rules=False
    jeufinal=False
    #creation de la fenetre et chargement des textures
    pygame.init()
    largeur, hauteur = 1000, 600
    fenetre = pygame.display.set_mode((largeur, hauteur))
    pygame.display.set_caption('CityQuizz')

    # Style des texte
    white = (255, 255, 255)
    couleur_texte_survol = ( 119 , 181 , 254)
    couleur_texte = white
    font = pygame.font.SysFont("comicsansms", 50)


    # fondu du lancement du jeu -------------------------------------------
    if intro==True:
        for i in range(1, 255, 2):
            r = abs(69 / 255 * i)
            g = abs(93 / 255 * i)
            b = abs(215/255*i)
            fenetre.fill((r, g, b))
            pygame.display.flip()
            time.sleep(0.001)
        intro=False
    #----------------------------------------------------------------------

    fenetre.fill((69, 93, 215))
    menu_principal = True

    # Texte à afficher
    texte = "Lancer le Jeu"
    texte_surface = font.render(texte, True, couleur_texte)
    texte_rect = texte_surface.get_rect()
    texte_rect.center = (largeur // 2, hauteur // 4)

    text_classement = "Voir les Regles du jeu"
    text_classement_surface = font.render(text_classement, True, couleur_texte)
    text_classement_rect = text_classement_surface.get_rect()
    text_classement_rect.center = (largeur // 2, hauteur // 2)

    nom_image = "images/logo201F.png"
    chemin_image = os.path.join("", nom_image)
    image = pygame.image.load(chemin_image)
    image = pygame.transform.scale(image, (100, 100))
    fenetre.blit(image, (largeur // 2 - 50 , hauteur * 3 // 4 - 50))

    pygame.display.set_icon(image)

    while menu_principal:
        fenetre.blit(texte_surface, texte_rect)
        fenetre.blit(text_classement_surface, text_classement_rect)
        for event in pygame.event.get():
            if event.type == QUIT:
                    menu_principal = False
                    menu=False
            elif event.type == KEYUP and event.key == K_ESCAPE:
                    menu_principal = False
                    menu=False

            # Survol des textes pour les faire changer de couleur ( pas fonctionnel )
            if event.type == pygame.MOUSEMOTION:
                if texte_rect.collidepoint(event.pos) :
                    couleur_texte = couleur_texte_survol
                else:
                    couleur_texte = white
                if text_classement_rect.collidepoint(event.pos) :
                    couleur_texte = couleur_texte_survol
                else:
                    couleur_texte = white
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                print("Clic de souris aux coordonnées :", x, y)
            
            

            # clique sur les textes pour passer d'un menu a l'autre ( fonctionnel )
            if event.type == pygame.MOUSEBUTTONDOWN:
                if texte_rect.collidepoint(event.pos):
                    menu_principal=False
                    choix_du_niveau=True
                    print("choix_du_niveau div")
                elif text_classement_rect.collidepoint(event.pos):
                    rules=True
                    menu_principal = False
                    print("rules div")
            else:
                pygame.display.flip()
            
    
    pygame.display.flip()
    while rules==True:
        regles('ville')
        regles('pays')
        
        rules = False
        menu_principal = True
    while choix_du_niveau==True:
        choix_niveau()
        choix_du_niveau = False
        menu_principal = True
    pygame.display.flip()
pygame.quit()