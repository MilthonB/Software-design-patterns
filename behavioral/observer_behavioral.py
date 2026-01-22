
from abc import ABC, abstractmethod

from typing import List

"""
Ejemplos de uso: El patrón Observer es bastante habitual en el código Python, sobre todo en los componentes GUI. 
Proporciona una forma de reaccionar a los eventos que suceden en otros objetos, sin acoplarse a sus clases.

Identificación: El patrón puede reconocerse por los métodos de subscripción, que almacenan objetos en una lista, y por las llamadas al 
método de actualización emitidas a todos los objetos de esa lista.

https://refactoring.guru/es/design-patterns/observer/python/example


"""


class Observer(ABC):

    @abstractmethod
    def update(self, message: str) -> None:
        ...



class EmailNotifier(Observer):
    def update(self, message: str) -> None:
        print(f"Email Notifier: {message}")


class SmsNotifier(Observer):
    def update(self, message: str) -> None:
        print(f"SMS Notifier: {message}")   



class NotifierEvent:
    def __init__(self) -> None:
        self.subscribers: List[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        self.subscribers.append(observer)

    def unsubscribe(self, observer: Observer) -> None:
        self.subscribers.remove(observer)

    def notify(self, message: str) -> None:
        for subscriber in self.subscribers:
            subscriber.update(message=message)



if __name__ == "__main__":

    emial_notifier = EmailNotifier()
    sms_notifier = SmsNotifier()

    notifier_event = NotifierEvent()

    notifier_event.subscribe(emial_notifier)
    notifier_event.subscribe(sms_notifier)

    notifier_event.notify("New user registered.")
