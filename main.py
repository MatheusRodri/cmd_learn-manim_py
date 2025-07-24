# Parei em 21:00 minutos
from manim import Scene, Circle, Square, Create,Transform

class Animacao(Scene):
    def construct(self):
        circulo = Circle() # Círculo
        quadrado = Square() # Quadrado

        self.play(Create(circulo)) # Cria o círculo na cena
        self.play(Transform(circulo, quadrado)) # Transforma o círculo em quadrado

