import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))

pygame.display.set_caption("Parkomat")
ikona = pygame.image.load("znak.png")
pygame.display.set_icon(ikona)
img1 = pygame.image.load("1.png")
img2 = pygame.image.load("2.png")
img5 = pygame.image.load("5.png")
img10 = pygame.image.load("10.png")
img20 = pygame.image.load("20.png")
img50 = pygame.image.load("50.png")

font = pygame.font.SysFont("comicsansms", 16)

text = font.render("złotówki", True, (200, 200, 200))


def rysuj():
    screen.blit(img1, (0, 200))
    screen.blit(img2, (32, 200))
    screen.blit(img5, (64, 200))
    screen.blit(img10, (0, 232))
    screen.blit(img20, (32, 232))
    screen.blit(img50, (64, 232))


running = True
while running:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    rysuj()
    screen.blit(text,(15,170))


    pygame.display.update()
