import pygame  # Importation du module pygame
import random  # Importation du module random

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre de jeu
SCREEN_WIDTH = 800  # Largeur de l'écran
SCREEN_HEIGHT = 400  # Hauteur de l'écran
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Création de la fenêtre de jeu

# Couleurs
WHITE = (255, 255, 255)  # Couleur blanche
BLACK = (0, 0, 0)  # Couleur noire

# Vitesse du jeu
game_speed = 10  # Vitesse de déplacement des obstacles

# Classe pour le dinosaure
class Dino(pygame.sprite.Sprite):  # Définition de la classe Dino qui hérite de pygame.sprite.Sprite
    def __init__(self):  # Initialisation de la classe
        super().__init__()  # Appel du constructeur de la classe parente
        self.image = pygame.Surface((50, 50))  # Création de l'image du dinosaure
        self.image.fill(BLACK)  # Remplissage de l'image avec la couleur noire
        self.rect = self.image.get_rect()  # Obtention du rectangle englobant l'image
        self.rect.x = 50  # Position initiale en x du dinosaure
        self.rect.y = SCREEN_HEIGHT - 100  # Position initiale en y du dinosaure
        self.is_jumping = False  # Indicateur de saut
        self.jump_speed = 15  # Vitesse de saut
        self.gravity = 1  # Gravité

    def update(self):  # Mise à jour de l'état du dinosaure
        keys = pygame.key.get_pressed()  # Récupération des touches pressées
        if keys[pygame.K_SPACE] and not self.is_jumping:  # Si la touche espace est pressée et que le dinosaure ne saute pas
            self.is_jumping = True  # Le dinosaure commence à sauter

        if self.is_jumping:  # Si le dinosaure est en train de sauter
            self.rect.y -= self.jump_speed  # Déplacement vers le haut
            self.jump_speed -= self.gravity  # Réduction de la vitesse de saut
            if self.jump_speed < -15:  # Si la vitesse de saut est inférieure à -15
                self.is_jumping = False  # Le dinosaure arrête de sauter
                self.jump_speed = 15  # Réinitialisation de la vitesse de saut

# Classe pour les obstacles
class Obstacle(pygame.sprite.Sprite):  # Définition de la classe Obstacle qui hérite de pygame.sprite.Sprite
    def __init__(self):  # Initialisation de la classe
        super().__init__()  # Appel du constructeur de la classe parente
        self.image = pygame.Surface((20, 40))  # Création de l'image de l'obstacle
        self.image.fill(BLACK)  # Remplissage de l'image avec la couleur noire
        self.rect = self.image.get_rect()  # Obtention du rectangle englobant l'image
        self.rect.x = SCREEN_WIDTH  # Position initiale en x de l'obstacle
        self.rect.y = SCREEN_HEIGHT - 90  # Position initiale en y de l'obstacle

    def update(self):  # Mise à jour de l'état de l'obstacle
        self.rect.x -= game_speed  # Déplacement vers la gauche
        if self.rect.x < -20:  # Si l'obstacle sort de l'écran
            self.rect.x = SCREEN_WIDTH  # Réinitialisation de la position en x
            self.rect.y = SCREEN_HEIGHT - 90  # Réinitialisation de la position en y

# Groupes de sprites
all_sprites = pygame.sprite.Group()  # Création du groupe de tous les sprites
obstacles = pygame.sprite.Group()  # Création du groupe des obstacles

# Création du dinosaure et des obstacles
dino = Dino()  # Création d'une instance de la classe Dino
all_sprites.add(dino)  # Ajout du dinosaure au groupe de tous les sprites

for _ in range(3):  # Boucle pour créer 3 obstacles
    obstacle = Obstacle()  # Création d'une instance de la classe Obstacle
    all_sprites.add(obstacle)  # Ajout de l'obstacle au groupe de tous les sprites
    obstacles.add(obstacle)  # Ajout de l'obstacle au groupe des obstacles

# Boucle principale du jeu
running = True  # Indicateur de fonctionnement du jeu
clock = pygame.time.Clock()  # Création d'une horloge pour contrôler la vitesse de la boucle

while running:  # Boucle principale du jeu
    for event in pygame.event.get():  # Récupération des événements
        if event.type == pygame.QUIT:  # Si l'événement est de type QUIT
            running = False  # Arrêt de la boucle principale

    # Mise à jour des sprites
    all_sprites.update()  # Mise à jour de tous les sprites

    # Détection des collisions
    if pygame.sprite.spritecollideany(dino, obstacles):  # Si le dinosaure entre en collision avec un obstacle
        running = False  # Arrêt de la boucle principale

    # Dessin des éléments à l'écran
    screen.fill(WHITE)  # Remplissage de l'écran avec la couleur blanche
    all_sprites.draw(screen)  # Dessin de tous les sprites sur l'écran
    pygame.display.flip()  # Mise à jour de l'affichage

    # Contrôle de la vitesse de la boucle
    clock.tick(30)  # Limitation de la vitesse de la boucle à 30 images par seconde

pygame.quit()  # Fermeture de Pygame