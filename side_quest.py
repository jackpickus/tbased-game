import pygame
pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Space Survival')

black = (0, 0, 0)
white = (255, 255, 255)

ship_width = 45
ship_height = 35

clock = pygame.time.Clock()

spaceshipImg = pygame.image.load('img/spaceship.png')
asteroidImg = pygame.transform.scale(pygame.image.load('img/asteroid.png'), (80, 100))

def spaceship(x, y):
    gameDisplay.blit(spaceshipImg, (x, y))

def asteriod(x, y):
    asteroidImg = pygame.transform.scale(pygame.image.load('img/asteroid.png'), (80, 100))
    gameDisplay.blit(asteroidImg, (x, y))

# space_ship_speed = 0 Not sure what this is
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
    y_change = 0

    playing = True

    while playing:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -5
                elif event.key == pygame.K_d:
                    x_change = 5
                elif event.key == pygame.K_s:
                    y_change = 5
                elif event.key == pygame.K_w:
                    y_change = -5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0
                elif event.key == pygame.K_s or event.key == pygame.K_w:
                    y_change = 0

        x += x_change
        y += y_change
            
        gameDisplay.fill(black)
        
        if x > display_width - ship_width:
            x = display_width - 45
        if x < 0:
            x = 0
        if y > display_height - ship_height:
            y = display_height - 30
        if y < 0:
            y = 0

        spaceship(x, y)
        asteriod(300, 300)

        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
