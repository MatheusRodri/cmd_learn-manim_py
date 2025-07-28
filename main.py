# Parei em 4:00 minutos
from manim import Scene, Circle, Square, Create,Transform

class Animacao(Scene):
    def construct(self):
        circulo = Circle() # Círculo
        quadrado = Square() # Quadrado

        self.play(Create(circulo)) # Cria o círculo na cena
        self.pause(3) # Pausa por 3 segundos
        self.play(Transform(circulo, quadrado)) # Transforma o círculo em quadrado