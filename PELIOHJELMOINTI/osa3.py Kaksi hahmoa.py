#Kaksi hahmoa
import pygame

naytto = pygame.display.set_mode((1800, 1800))
pygame.display.set_caption("Piirtäminen")

def piirraKuva(kuvatiedosto, x, y):
    naytto.blit(kuvatiedosto, (x, y))

def piirtaminen(naytto, hahmot):
    naytto.fill((0, 0, 0))
    for hahmo in hahmot:
        if hahmo[3] == True:
            kuva = pygame.image.load(hahmo[0]).convert()
            naytto.blit(kuva, (hahmo[1], hahmo[2]))
    pygame.display.flip()

def kontrolli(hahmot, tapahtuma):
    if tapahtuma.type == pygame.KEYDOWN:
        if tapahtuma.key == pygame.K_SPACE:
            hahmot[0][3] = True
            hahmot[1][3] = True 

def main():
    kissahahmo = ["cat.png", 100, 100, False]
    sotilashahmo = ["Sotilas.png", 200, 150, False] 
    hahmot = [kissahahmo, sotilashahmo]
    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break
        kontrolli(hahmot, tapahtuma)
        piirtaminen(naytto, hahmot) 

main() 
