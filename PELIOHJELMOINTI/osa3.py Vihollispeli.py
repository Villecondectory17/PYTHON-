#Vihollispeli
import pygame
import random

naytto = pygame.display.set_mode((640, 400)) 
pygame.display.set_caption("Piirtäminen")

def piirtaminen(naytto, hahmot, viholliset): 
    naytto.fill((0, 0, 0))
    for hahmo in hahmot:
        if hahmo[3] == True:
            kuva = pygame.image.load(hahmo[0]).convert()
            naytto.blit(kuva, (hahmo[1], hahmo[2]))
    for vihollinen in viholliset:
        if vihollinen[3] == True:
            kuva = pygame.image.load(vihollinen[0]).convert()
            naytto.blit(kuva, (vihollinen[1], vihollinen[2])) 
    pygame.display.flip()

def kontrolli(hahmot, tapahtuma, viholliset): 
    for vihollinen in viholliset: 
        hahmo = hahmot[0]
        if (vihollinen[1] == hahmo[1]) and (vihollinen[2] == hahmo[2]): 
            del hahmot[0] 
    if tapahtuma.type == pygame.KEYDOWN:
        if tapahtuma.key == pygame.K_SPACE:
            for hahmo in hahmot:
                hahmo[3] = True 
            for vihollinen in viholliset:
                vihollinen[3] = True
        elif tapahtuma.key == pygame.K_RIGHT:
            päähahmo = hahmot[0]
            päähahmo[1] += 10 
        elif tapahtuma.key == pygame.K_LEFT:
            päähahmo = hahmot[0] 
            päähahmo[1] += -10
        elif tapahtuma.key == pygame.K_DOWN: 
            päähahmo = hahmot[0]
            päähahmo[2] += 10 
        elif tapahtuma.key == pygame.K_UP:
            päähahmo = hahmot[0]
            päähahmo[2] += -10 
        else: 
            return 

def main():
    kissahahmo = ["cat.png", 0, 0, False]
    sotilashahmo = ["Sotilas.png", 100, 0, False]    
    hahmot = [kissahahmo, sotilashahmo]
    vihollinen1 = ["Animaatiosotilas.png", 150, 200, True] 
    vihollinen2 = ["Animaatiosotilaat.png", 350, 200, True]
    vihollinen3 = ["Vihollinen.jpg", 550, 200, True] 
    viholliset = [vihollinen1, vihollinen2, vihollinen3] 
    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break 
        for vihollinen in viholliset:
            #del hahmot[0] 
        
            if vihollinen[1] > 640:
                vihollinen[1] = 0 
                vihollinen[2] = random.randint(0, 400)
            else:
                vihollinen[1] += 0.5
            
        kontrolli(hahmot, tapahtuma, viholliset)
        piirtaminen(naytto, hahmot, viholliset) 
main()  
