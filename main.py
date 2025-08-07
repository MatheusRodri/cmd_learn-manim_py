from manim import Scene, Circle, Square, Create,Transform # Import de Funções que serão usadas
from manim import BLUE # Import de Cores do próprio manim

# Cria uma classe de cena que herda de Scene
class Animacao(Scene):
    def construct(self):
        circulo = Circle() # Cria um círculo
        quadrado = Square(color=BLUE) # Cria um quadrado


        self.add(circulo) # Adiciona o círculo à cena
        self.add(quadrado) # Adiciona o quadrado à cena
        self.bring_to_back(quadrado) # Coloca o objeto no fundo

        self.pause(1) # Pausa por 1 segundo
        self.remove(quadrado) # Remove o quadrado da cena
        self.wait(2) # Espera 2 segundos antes de continuar
        self.remove(circulo) # Remove o círculo da cena

        self.pause(1) # Pausa por 1 segundo


        self.play(Create(circulo)) # Cria o círculo na cena
        self.play(Transform(circulo, quadrado)) # Transforma o círculo em quadrado

        self.wait(2) # Espera 2 segundos antes de terminar a cena

        