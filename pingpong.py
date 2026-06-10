from pygame import *
from time import time as timer

pantalla = display.set_mode((700,500))
display.set_caption("juego")
fondo = transform.scale(image.load('color1.png'),(700,500))

juego = True

class GameSprite(sprite.Sprite):
    def __init__(self, velocidad, imagen, ancho, largo, posicionX, posicionY, jugadores):

        self.image = transform.scale(image.load(imagen),(ancho,largo))
        self.vy = velocidad
        self.pX = posicionX
        self.pY = posicionY
        self.ej = jugadores

    def reset(self):
        pantalla.blit(self.image,(self.pX, self.pY ))

class Jugador(GameSprite):
    
    def mover(self):
        if self.ej == 1:
            teclado = key.get_pressed()

            if teclado[K_w]:
                self.pY -= self.vy

            if teclado[K_s]:
                self.pY += self.vy

        if self.ej == 2:
            teclado = key.get_pressed()
            if teclado[K_UP]:
                self.pY -= self.vy

            if teclado[K_DOWN]:
                self.pY += self.vy

        


bloque1 = Jugador(5,'Bloque.png',40,100,-20,25,1)           
bloque2 = Jugador(5,'Bloque.png',40,100,680,425,2)

clock = time.Clock()

while juego:
    for e in event.get():
        if e.type == QUIT:
            juego = False

    pantalla.blit(fondo,(0,0))

    bloque1.reset()
    bloque1.mover()

    bloque2.reset()
    bloque2.mover()
    

    display.update()
    clock.tick(60)
