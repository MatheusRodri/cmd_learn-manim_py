# Parei em 45:00 minutos
from manim import Scene # Import de Funções que serão usadas
from manim import Text,Create, Rectangle, Uncreate # Import de Funções que serão usadas
from manim import ORANGE

class Animacao(Scene): # Cria uma classe de cena que herda de Scene
    def construct(self):
        t = Text("Olá, Manim!",color='#fff') # Cria um texto
        t2 = Text("Fala Matheus !", color='#fff') # Cria um segundo texto
        r = Rectangle(color=ORANGE).scale(2) # Cria um retângulo

        self.camera.background_color = '#000' # Define a cor de fundo da cena
        self.play(Create(t)) # Cria o texto na cena
        self.wait(1)
        self.play(Create(r))

        self.play(
            Uncreate(t),
            Create(t2),
        )
        self.wait(1)
        self.play(
            Uncreate(t2),
            Uncreate(r)
        )