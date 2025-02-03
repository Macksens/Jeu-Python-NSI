import pygame
import numpy as np
import random

# Initialisation de Pygame
pygame.init()

# Paramètres du jeu
WIDTH, HEIGHT = 800, 400
GROUND = HEIGHT - 50
DINO_X = 50
OBSTACLE_WIDTH = 40
OBSTACLE_HEIGHT = 50
OBSTACLE_X = WIDTH
OBSTACLE_SPEED = 5
GRAVITY = 1
JUMP_STRENGTH = -15

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Création de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Q-learning paramètres
alpha = 0.1   # Taux d'apprentissage
gamma = 0.9   # Facteur d'actualisation
epsilon = 1.0 # Exploration (diminue au fil du temps)
epsilon_decay = 0.995
q_table = {}

# Fonction pour obtenir l'état
def get_state(dino_y, obstacle_x):
    return (dino_y, obstacle_x)

# Initialisation du dino
class Dino:
    def __init__(self, color=WHITE):
        self.color = color
        self.y = GROUND
        self.velocity = 0
        self.on_ground = True

    def jump(self):
        if self.on_ground:
            self.velocity = JUMP_STRENGTH
            self.on_ground = False

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

        if self.y >= GROUND:
            self.y = GROUND
            self.on_ground = True

# Initialisation de l'obstacle
class Obstacle:
    def __init__(self):
        self.x = OBSTACLE_X

    def update(self):
        self.x -= OBSTACLE_SPEED
        if self.x < 0:
            self.x = WIDTH

# Boucle d'entraînement du Q-learning
episodes = 5000
for episode in range(episodes):
    dino = Dino()
    obstacle = Obstacle()
    done = False
    total_reward = 0
    
    while not done:
        state = get_state(dino.y, obstacle.x)

        # Initialiser l'état s'il est absent de la Q-table
        if state not in q_table:
            q_table[state] = [0, 0]  # [Ne rien faire, Sauter]

        # Sélection de l'action (exploitation/exploration)
        if random.uniform(0, 1) < epsilon:
            action = random.choice([0, 1])  # Exploration
        else:
            action = np.argmax(q_table[state])  # Exploitation

        # Effectuer l'action
        if action == 1:
            dino.jump()

        # Mettre à jour le jeu
        dino.update()
        obstacle.update()

        # Calculer la récompense
        next_state = get_state(dino.y, obstacle.x)
        if next_state not in q_table:
            q_table[next_state] = [0, 0]

        if obstacle.x < DINO_X + 40 and dino.y >= GROUND:
            reward = -100  # Collision
            done = True
        else:
            reward = 1  # Récompense pour rester en vie

        # Mise à jour de la Q-table
        q_table[state][action] = q_table[state][action] + alpha * (
            reward + gamma * max(q_table[next_state]) - q_table[state][action]
        )

        total_reward += reward

    # Réduction progressive de epsilon
    epsilon *= epsilon_decay

    # Afficher la progression
    if episode % 500 == 0:
        print(f"Épisode {episode}, Total Reward: {total_reward}, Epsilon: {epsilon:.3f}")

print("Entraînement terminé!")

