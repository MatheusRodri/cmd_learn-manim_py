from manim import ThreeDScene # Import de Funções que serão usadas
from manim import Text,Create, Rectangle, Uncreate # Import de Funções que serão usadas
from manim import ORANGE # Import de Cores que serão usadas

class Animacao(ThreeDScene): # Cria uma classe de cena que herda de Scene
    def construct(self): # Método construtor da classe
        t = Text("Olá, Manim!",color='#fff') # Cria um texto
        t2 = Text("Fala Matheus !", color='#fff') # Cria um segundo texto
        r = Rectangle(color=ORANGE).scale(2) # Cria um retângulo

        self.camera.background_color = '#000' # Define a cor de fundo da cena
        self.play(Create(t)) # Cria o texto na cena
        self.wait(1) # Espera 1 segundo
        self.play(Create(r)) # Cria o retângulo na cena
 
        self.play(
            Uncreate(t), # Remove o texto 1 da cena
            Create(t2),  # Cria o texto 2 na cena
        )
        
        self.wait(1) # Espera 1 segundo

        self.play(
            Uncreate(t2), # Remove o texto 2 da cena
            Uncreate(r)   # Remove o retângulo da cena
        )