
"""
Ejemplos de uso: El patrón Factory Method se utiliza mucho en el código Python. Resulta muy útil cuando necesitas proporcionar un alto nivel 
de flexibilidad a tu código.

Identificación: Los métodos fábrica pueden ser reconocidos por métodos de creación, que crean objetos de clases concretas, 
pero los devuelven como objetos del tipo abstracto o interfaz.

https://refactoring.guru/es/design-patterns/factory-method/python/example
"""

from abc import ABC, abstractmethod

class DeparmentEntity():
    id:int
    name:str
    role:str

    def __init__(self, id:int, name:str, role:str) -> None:
        self.id = id
        self.name = name
        self.role = role


class Deparment(ABC):
    

    @abstractmethod
    def deparment(self) -> DeparmentEntity:
        ...

    def info_deparment(self) -> object:

        deparment_new: DeparmentEntity = self.deparment()

        result  = {
            "Id" : deparment_new.id,
            "name": deparment_new.name,
            "role": deparment_new.role
        }

        return result


class ITDeparment(Deparment):

    def deparment(self) -> DeparmentEntity:
        return DeparmentEntity(
            id=1,
            name="TI",
            role="Tecnologia"
        )

class RHDeparment(Deparment):

    def deparment(self) -> DeparmentEntity:
        return DeparmentEntity(
            id=2,
            name="Recursos Humanos",
            role="Adminstracion"
        )



def create_deparment(deparment: Deparment) -> str:

    return f"Infromacion del departemaneto {deparment.info_deparment()}"


if __name__ == "__main__":
    print("creaccion de departamento TI")
    d1 = create_deparment(deparment=ITDeparment())
    print(d1)

    print("Creacion de departamento RH")
    d2 = create_deparment(deparment=RHDeparment())
    print(d2)