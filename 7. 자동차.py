'''
자동차
'''
import pygame
pygame.init() # 초기화
# Built draws the image to the screen
def car(carImg, x, y):
    gameDisplay.blit(carImg, (x, y))

display_width = 800
display_height = 600

car_width = 179

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('race')

white = (255, 255, 255)

clock = pygame.time.Clock()
crashed = False
carImg = pygame.image.load('./racecar.png')

x = (display_width * 0.45) # 10
y = (display_height * 0.8) # 10
x_change = 0
car_speed = 0
y_change = 0

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5

            if event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                y_change = 0

    x += x_change
    y += y_change
    gameDisplay.fill(white)
    car(carImg, x, y)

    if x > display_width - car_width or x < 0:
        crashed = True

    pygame.display.update()
    clock.tick(60)

