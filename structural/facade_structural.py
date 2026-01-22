


"""

Ejemplos de uso: El patrón Facade se utiliza habitualmente en aplicaciones escritas en Python. Es de especial utilidad al trabajar con 
bibliotecas y API complejas.

Identificación: El patrón Facade se puede reconocer en una clase con una interfaz simple, pero que delega la mayor parte del trabajo 
a otras clases. Normalmente, las fachadas gestionan todo el ciclo de vida de los objetos que utilizan.


https://refactoring.guru/es/design-patterns/facade/python/example

Pricipios SOLID aplciados son:

- OCP
- SRP
- DIP

"""

from abc import ABC, abstractmethod

class Build(ABC):
    @abstractmethod
    def build_piece(self, piece: str) -> str:
        ...

class GeardBuild(Build):
    def build_piece(self, piece: str) -> str:
        return f"Construyendo pieza de engranaje: {piece}"

class SprocketBuild(Build):
    def build_piece(self, piece: str) -> str:
        return f"Construyendo pieza de piñón: {piece}"

class ChainBuild(Build):
    def build_piece(self, piece: str) -> str:
        return f"Construyendo pieza de cadena: {piece}" 


class BikeFacade:
    def __init__(self, geard_builder: GeardBuild, sprocket_builder: SprocketBuild, chain_builder: ChainBuild) -> None:
        self.geard_builder = geard_builder
        self.sprocket_builder = sprocket_builder
        self.chain_builder  = chain_builder

    def build_bike(self) -> str:

        geard: str = self.geard_builder.build_piece("Engranaje de 21 velocidades")
        sprocket: str = self.sprocket_builder.build_piece(piece=geard)
        chain: str = self.chain_builder.build_piece(piece=sprocket)



        return f"Proceso de construcción de bicicleta:\n{geard}\n{sprocket}\n{chain}\nBicicleta construida con éxito."




if __name__ == "__main__":

    geard_builder = GeardBuild()
    sprocket_builder = SprocketBuild()
    chain_builder = ChainBuild()


    bike_facade = BikeFacade(chain_builder=chain_builder, geard_builder=geard_builder, sprocket_builder=sprocket_builder)
    result = bike_facade.build_bike()
    print(result)

