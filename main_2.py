# Parei em 4:00 minutos
from manim import Scene # Import de Funções que serão usadas
from manim import Text,Create, Rectangle, Uncreate # Import de Funções que serão usadas

class Animacao(Scene): # Cria uma classe de cena que herda de Scene
    def construct(self):
        t = Text("Olá, Manim!",color='#40126f') # Cria um texto
        t2 = Text("Fala Matheus !", color='#000') # Cria um segundo texto
        r = Rectangle(color='#40126f') # Cria um retângulo

        self.camera.background_color = '#ff8972' # Define a cor de fundo da cena
        self.play(Create(t)) # Cria o texto na cena
        self.wait()
        self.play(Create(r))

        self.play(
            Uncreate(t),
            Create(t),
        )
        self.wait()
        self.play(
            Uncreate(t2),
            Uncreate(r)
        )