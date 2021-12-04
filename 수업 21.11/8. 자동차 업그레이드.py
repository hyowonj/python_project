'''
자동차 업그레이드
'''
import pygame
pygame.init()
display_width = 800
display_height = 600

while True:
    count = 0
    temp_id = input("Enter your id: ")
    if len(temp_id) < 8:
        count = 1
        print("try another one")
    if count == 0:
        print("ok")
        temp_pwd = input("Enter your pwd: ")
        break
print("You made it! id: {}, pwd: {}".format(temp_id, temp_pwd))

a = int(input("자동차를 선택하세요. red(1), blue(2)."))
if a == 1:
    racecar = pygame.image.load('./racecar_1.png')
if a == 2:
    racecar = pygame.image.load('./racecar_2.png')

black = (0, 0, 0)
green = (143, 188, 143)

car_width = 179

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit racey')
clock = pygame.time.Clock()
carImg = racecar

def car(carImg, x, y):
    gameDisplay.blit(carImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()

def crash():
    message_display('You gg')

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    y_change = 0
    x_change = 0
    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
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
        gameDisplay.fill(green)
        car(carImg, x, y)
        if x > display_width - car_width or x < 0:
            crash()
        pygame.display.update()
        clock.tick(60)
game_loop()
pygame.quit()
quit()
