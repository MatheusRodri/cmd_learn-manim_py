# Parei em 4:00 minutos
from manim import Scene, Circle, Square, Create,Transform

# Cria uma classe de cena que herda de Scene
class Animacao(Scene):
    def construct(self):
        circulo = Circle() # Cria um círculo
        quadrado = Square() # Cria um quadrado

        self.play(Create(circulo)) # Cria o círculo na cena
        self.pause(3) # Pausa por 3 segundos
        self.play(Transform(circulo, quadrado)) # Transforma o círculo em quadrado