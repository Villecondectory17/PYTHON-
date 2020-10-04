# Kuvan piirtävä funktio
import pygame
import random

# Alusta ikkuna 
naytto = pygame.display.set_mode((640, 400))
pygame.display.set_caption("Piirtäminen") 
naytto.fill((0, 0, 0))

def piirraKuva(kuvatiedosto, x, y):
    """Piirretään ruudulle kohtaan x,y kuva käyttäen kuvatiedostoa."""
    kuva = pygame.image.load(kuvatiedosto).convert() 
    naytto.blit(kuva, (x, y))
    pygame.display.flip()


def main():

    x = 320
    y = 200

    while True:
        tapahtuma = pygame.event.poll()
        if tapahtuma.type == pygame.QUIT:
            break
        
        x = random.randint(0, 640)
        y = random.randint(0, 400)
        piirraKuva("cat.png", x, y)
        
main()
