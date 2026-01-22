
from abc import ABC, abstractmethod

"""

Ejemplos de uso: El patrón Decorator es bastante común en el código Python, especialmente en el código relacionado con los flujos (streams).

Identificación: El patrón Decorator puede ser reconocido por métodos de creación o el constructor que acepta objetos de la misma clase o 
interfaz que la clase actual.


https://refactoring.guru/es/design-patterns/decorator/python/example


Aplicaicon  de principios solid 

DI
Open/Closed
Alta composion y baja herencia
"""


class Notifier(ABC):

    @abstractmethod
    def send(self, message: str) -> None:
        ...

class EmitterEmail:

    def __init__(self, notifier_email: Notifier, notifier_sms: Notifier) -> None:
        self.notifier_email = notifier_email
        self.notifier_sms = notifier_sms
 
    def send_all_notifiers(self, message:str) -> None:
        self.notifier_email.send(message)
        self.notifier_sms.send(message)


class NotifierEmail(Notifier):

    def send(self, message: str) -> None:
        print(f"Enviando email con el mensaje: {message}")

class NotifierSMS(Notifier):

    def send(self, message: str) -> None:
        print(f"Enviando SMS con el mensaje: {message}")



if __name__ == "__main__":
    notifier_email = NotifierEmail()
    notifier_sms = NotifierSMS()

    emitter = EmitterEmail(notifier_email=notifier_email, notifier_sms=notifier_sms)
    emitter.send_all_notifiers("Hola este es un mensaje importante")