#Hahmon liikkumisen rajaus näytölle 
import pygame

naytto = pygame.display.set_mode((800, 800)) 
pygame.display.set_caption("Piirtäminen")
#viholliset = [["vihollinen.png", 200, 200]] 
 
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
           for hahmo in hahmot:
               hahmo[3] = True
        elif tapahtuma.key == pygame.K_RIGHT: 
            päähahmo = hahmot[0]
            if päähahmo[1] < 745: 
                päähahmo[1] += 10 
        elif tapahtuma.key == pygame.K_LEFT: 
            päähahmo = hahmot[0] 
            if päähahmo[1] > 10: 
                päähahmo[1] += -10 
        elif tapahtuma.key == pygame.K_DOWN: 
            päähahmo = hahmot[0]
            if päähahmo[2] < 745: 
                päähahmo[2] += 10
        elif tapahtuma.key == pygame.K_UP:
            päähahmo = hahmot[0]
            if päähahmo[2] > 10: 
                päähahmo[2] += -10 
        else:
            return 

def main():
    kissahahmo = ["Smiley_cat.png", 150, 150, False] 
    Ritarihahmo = ["Ritarihahmo.jpg", 100, 150, False] 
    hahmot = [kissahahmo, Ritarihahmo] 
    while True: 
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT: 
            break
        kontrolli(hahmot, tapahtuma) 
        piirtaminen(naytto, hahmot) 

main() 

