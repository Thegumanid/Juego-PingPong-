from pygame import *

pantalla = display.set_mode((700, 500))
display.set_caption("juego")
fondo = transform.scale(image.load('color1.png'),(700,500))

class GameSprite(sprite.Sprite):
    
    def __init__(self, velocidad, imagen, ancho, largo, posicionX, posicionY, jugadores):
        
        self.image = transform.scale(image.load(imagen), (ancho, largo))
        self.rect = self.image.get_rect() 
        self.rect.x = posicionX
        self.rect.y = posicionY
        self.vy = velocidad
        self.ej = jugadores 

    def reset(self):
        pantalla.blit(self.image, (self.rect.x, self.rect.y))

class Jugador(GameSprite):
    def mover(self):
        teclado = key.get_pressed()
        if self.ej == 1:
            if teclado[K_w] and self.rect.y > 0:
                self.rect.y -= self.vy
            if teclado[K_s] and self.rect.y < 400:
                self.rect.y += self.vy

        if self.ej == 2:
            if teclado[K_UP] and self.rect.y > 0:
                self.rect.y -= self.vy
            if teclado[K_DOWN] and self.rect.y < 400:
                self.rect.y += self.vy


class Pelota(GameSprite):
    def __init__(self, velocidad_x, velocidad_y, imagen, ancho, largo, pX, pY):
        super().__init__(velocidad_y, imagen, ancho, largo, pX, pY, 0)

        self.vx = velocidad_x
        self.vy = velocidad_y

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        
        # Rebote arriba y abajo
        if self.rect.y <= 0 or self.rect.y >= 450:
            self.vy *= -1
        
    def resset(self):

        if self.rect.x <= 0 or self.rect.x >= 680:
            return True
        
        return False



bloque1 = Jugador(5, 'Bloque.png', 40, 100, 10, 200, 1)           
bloque2 = Jugador(5, 'Bloque.png', 40, 100, 650, 200, 2)
pelota = Pelota(4, 4, 'Pelota.png', 40, 40, 330, 230)

juego = True
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
    
    pelota.reset()
    pelota.update()
    pelota.resset()

    # Colisión con bloques
    if sprite.collide_rect(pelota, bloque1) or sprite.collide_rect(pelota, bloque2):
        pelota.vx *= -1

    if pelota.resset():
        juego = False

    display.update()
    clock.tick(60)

quit()
