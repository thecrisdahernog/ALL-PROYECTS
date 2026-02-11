class Libro:
    def __init__(self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        
    def MostrarInformacion(self):
        print(f"titulo: {self.titulo}")
        print(f"autor: {self.autor}")
        print(f"genero: {self.genero}")

#crear un objeto o una instancia
ObjetoLibro1 = Libro("el gran gatsby", "f. scott", "Ficcion")
ObejtoLibro2 = Libro("Titanic", "Leonardo Dicaprio", "Ficción") 

#acceder a los atributos de la clase
print(ObjetoLibro1.autor)

#acceder a los metodos de la clase
ObjetoLibro1.MostrarInformacion()
ObejtoLibro2.MostrarInformacion()