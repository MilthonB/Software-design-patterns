"""
Command Pattern

Este patrón encapsula una acción como un objeto (Command), 
permitiendo que diferentes invocadores (como endpoints o botones) 
la ejecuten sin conocer los detalles de su implementación.

Ventajas:
- Desacopla el invocador del receptor real.
- Permite almacenar, apilar o ejecutar acciones de forma diferida.
- Facilita reintentos, undo/redo, logging centralizado o batch processing.

Uso típico en APIs o sistemas event-driven:
- Recibir solicitudes y ponerlas en una cola para procesarlas después.
- Worker ejecuta los comandos uno por uno de manera controlada.



Ejemplos de uso: El patrón Command es muy común en el código Python. 
La mayoría de las veces se utiliza como alternativa a las retrollamadas (callbacks) para parametrizar elementos UI con acciones. 
También se utiliza para poner tareas en cola, realizar el seguimiento del historial de operaciones, etc.

Identificación: El patrón Command es reconocible por los métodos de comportamiento en un tipo de clase abstracta/interfaz 
(emisora) que invoca un método en una implementación de un tipo de clase abstracta/interfaz diferente (receptora) que la 
implementación del comando ha implementado durante su creación. Las clases de comando se limitan normalmente a acciones específicas.


https://refactoring.guru/es/design-patterns/command/python/example

"""
from abc import ABC, abstractmethod
from typing import List

class PaymentCommand(ABC):
    @abstractmethod
    def execute(self) -> str:
        ... 


class MercadoPagoProcess:
    def process_payment(self, amount: float, reference: str) -> str:
        return f"Procesando pago de {amount} a {reference} via MercadoPago"


class MercadoPagoPaymentCommand(PaymentCommand):
    def __init__(self, amount: float, reference: str, procesor: MercadoPagoProcess) -> None:
        self.amount = amount
        self.reference = reference
        self.procesor = procesor

    def execute(self) -> str:
        return self.procesor.process_payment(self.amount, self.reference)


class PaymentInvoker:
    def __init__(self) -> None:
        self._add_command: List[PaymentCommand] = []

    def add_command(self, command: PaymentCommand) -> None:
        self._add_command.append(command)

    def execute_commands(self) -> None:
        for command in self._add_command:
            result = command.execute()
            print(result)
            

if __name__ == "__main__":
    mercado_pago_processor = MercadoPagoProcess()

    command1: PaymentCommand = MercadoPagoPaymentCommand(amount=150.0, reference="REF123", procesor=mercado_pago_processor)
    command2: PaymentCommand = MercadoPagoPaymentCommand(amount=250.0, reference="REF456", procesor=mercado_pago_processor)

    invoker = PaymentInvoker()
    invoker.add_command(command1)
    invoker.add_command(command2)
    
    invoker.execute_commands()