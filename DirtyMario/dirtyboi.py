import pygame
import random
import time

pygame.init()

# Screen Setup
WIDTH, HEIGHT = 960, 640
TILE_SIZE = 40
ROWS = HEIGHT // TILE_SIZE
COLS = WIDTH // TILE_SIZE
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Platformer Enemies")
clock = pygame.time.Clock()

# Colors
WHITE, GREEN, RED, BROWN, BLACK, GRAY, BLUE, ORANGE = (255,255,255), (50,205,50), (255,50,50), (139,69,19), (0,0,0), (160,160,160), (0,0,255), (255,165,0)

# Level: 1 = block, 0 = pit/empty
level = [[1 if r == ROWS-1 else 0 for c in range(COLS)] for r in range(ROWS)]

class Entity(pygame.Rect):
    def __init__(self, x, y, w=30, h=40, color=GREEN):
        super().__init__(x, y, w, h)
        self.color = color
        self.vel_y = 0
        self.on_ground = False

    def apply_gravity(self):
        self.vel_y += 0.5
        self.y += self.vel_y
        self.on_ground = False

        if self.collides():
            self.y -= self.vel_y
            self.vel_y = 0
            self.on_ground = True

    def collides(self):
        for r in range(ROWS):
            for c in range(COLS):
                if level[r][c]:
                    block = pygame.Rect(c*TILE_SIZE, r*TILE_SIZE, TILE_SIZE, TILE_SIZE)
                    if self.colliderect(block):
                        return True
        return False

    def draw(self):
        pygame.draw.rect(screen, self.color, self)

class Player(Entity):
    def handle_input(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= 5
        if keys[pygame.K_RIGHT]:
            self.x += 5
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = -12

class Enemy(Entity):
    def __init__(self, x, y, behavior='chaser'):
        color = RED if behavior == 'chaser' else BLUE if behavior == 'camper' else ORANGE
        super().__init__(x, y, color=color)
        self.behavior = behavior
        self.dir = random.choice([-1, 1])
        self.jump_timer = 0

    def update(self, player):
        if self.behavior == 'chaser':
            self.chase(player)
        elif self.behavior == 'camper':
            self.camp(player)
        elif self.behavior == 'bouncer':
            self.bounce()
        self.apply_gravity()

    def is_safe(self, offset):
        ahead_x = self.centerx + offset
        ahead_y = self.bottom + 5
        grid_x = ahead_x // TILE_SIZE
        grid_y = ahead_y // TILE_SIZE
        if 0 <= grid_x < COLS and 0 <= grid_y < ROWS:
            return level[grid_y][grid_x] == 1
        return False

    def chase(self, player):
        if abs(player.x - self.x) > 5:
            self.dir = 1 if player.x > self.x else -1
            if self.is_safe(self.dir * 20):
                self.x += self.dir * 2
            elif self.on_ground:
                self.vel_y = -10

    def camp(self, player):
        if self.on_ground and self.is_safe(self.dir * 20) and random.random() < 0.005:
            self.dir *= -1
        self.x += self.dir

    def bounce(self):
        self.x += self.dir
        self.jump_timer += 1
        if self.jump_timer > 60 and self.on_ground:
            self.vel_y = -12
            self.jump_timer = 0

    # Placeholder: input vector for future neural net
    def get_input_vector(self, player):
        dx = (player.x - self.x) / WIDTH
        dy = (player.y - self.y) / HEIGHT
        pit_left = not self.is_safe(-20)
        pit_right = not self.is_safe(20)
        return [dx, dy, int(pit_left), int(pit_right)]

# Game State
player = Player(100, HEIGHT - 120)
enemies = [
    Enemy(600, HEIGHT - 120, 'chaser'),
    Enemy(400, HEIGHT - 120, 'camper'),
    Enemy(300, HEIGHT - 120, 'bouncer')
]

edit_mode = False
last_toggle = 0

def draw_grid():
    for r in range(ROWS):
        for c in range(COLS):
            if level[r][c]:
                pygame.draw.rect(screen, BROWN, (c*TILE_SIZE, r*TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, GRAY, (c*TILE_SIZE, r*TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

running = True
while running:
    screen.fill(WHITE)
    draw_grid()
    keys = pygame.key.get_pressed()

    # Prevent rapid toggling of edit mode
    if keys[pygame.K_TAB] and time.time() - last_toggle > 0.3:
        edit_mode = not edit_mode
        last_toggle = time.time()

    if edit_mode:
        mx, my = pygame.mouse.get_pos()
        grid_x = mx // TILE_SIZE
        grid_y = my // TILE_SIZE

        if grid_y < ROWS - 1:  # lock bottom row
            if pygame.mouse.get_pressed()[0]:
                level[grid_y][grid_x] = 1
            elif pygame.mouse.get_pressed()[2]:
                level[grid_y][grid_x] = 0
    else:
        player.handle_input(keys)
        player.apply_gravity()
        player.draw()

        for enemy in enemies:
            enemy.update(player)
            enemy.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
