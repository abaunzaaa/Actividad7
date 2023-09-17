from dataclasses import dataclass
@dataclass
class Elemento:
    nombre: str

    def igualdad (self, otro):
        if isinstance(otro, Elemento):
            return self.nombre == otro.nombre
        return False

class Conjunto:
    contador = 0

    def __init__(self, nombre): 
        self.elementos = [] 
        self.nombre = nombre
        Conjunto.contador += 1
        self.__id = Conjunto.contador
 

    def id(self):
        return self.__id

    def contiene(self, elemento):
        return any(e == elemento for e in self.elementos)

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        nuevo_conjunto = Conjunto(f"{self.nombre} UNION {otro_conjunto.nombre}")
        for elemento in self.elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        for elemento in otro_conjunto.elementos:
            nuevo_conjunto.agregar_elemento(elemento)
        return nuevo_conjunto

    def __add__(self, otro_conjunto):
        return self.unir(otro_conjunto)

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        elementos_comunes = [elem for elem in conjunto1.elementos if conjunto2.contiene(elem)]
        nombre_resultado = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        resultado = Conjunto(nombre_resultado)
        resultado.elementos = elementos_comunes
        return resultado

    def __str__(self): 

        elementos_str = ", ".join(elemento.nombre for elemento in self.elementos)
        return f"Conjunto {self.nombre}: ({elementos_str})"

Conjunto1 = Conjunto("A")
Conjunto2 = Conjunto("B")

Elemento_Uno = Elemento("1")
Elemento_Dos = Elemento("2")
Elemento_Tres = Elemento("3")

interseccion = Conjunto.intersectar(Conjunto1, Conjunto2)
print(interseccion)
Conjunto1.agregar_elemento(Elemento_Uno) 
Conjunto1.agregar_elemento(Elemento_Dos)
Conjunto2.agregar_elemento(Elemento_Tres)
Union_conjuntos = Conjunto1 + Conjunto2
print(Union_conjuntos)
