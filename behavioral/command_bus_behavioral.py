"""
Command Bus

El Command Bus es un patrón que centraliza la ejecución de comandos en un sistema. 
Permite registrar un handler para cada tipo de comando y luego enviar cualquier comando 
al bus, sin que el invocador conozca la implementación concreta del handler.

Ventajas:
- Desacopla completamente al invocador del receptor.
- Permite añadir funcionalidades transversales de manera centralizada 
  (como logging, colas, reintentos o validaciones).
- Facilita la escalabilidad en sistemas complejos con muchos tipos de comandos.

Uso típico:
- APIs complejas donde múltiples comandos deben ejecutarse de forma controlada.
- Sistemas event-driven, CQRS, o donde se requiere un manejo centralizado de acciones.
"""


from abc import ABC, abstractmethod
from typing import Dict, Type

class PaymentCommand(ABC):
    @abstractmethod
    def execute(self) -> str:
        ... 


class MercadoPagoProcess:
    def process_payment(self, amount: float, reference: str) -> str:
        return f"Procesando pago de {amount} a {reference} via MercadoPago"

class PayPalPagoProcess:
    def process_payment(self, amount: float, reference: str) -> str:
        return f"Procesando pago de {amount} a {reference} via PayPal"


class MercadoPagoPaymentCommand(PaymentCommand):
    def __init__(self, amount: float, reference: str, procesor: MercadoPagoProcess) -> None:
        self.amount = amount
        self.reference = reference
        self.procesor = procesor

    def execute(self) -> str:
        return self.procesor.process_payment(self.amount, self.reference)

class PaypalPaymentCommand(PaymentCommand):
    def __init__(self, amount: float, reference: str, procesor: PayPalPagoProcess) -> None:
        self.amount = amount
        self.reference = reference
        self.procesor = procesor

    def execute(self) -> str:
        return self.procesor.process_payment(self.amount, self.reference)


class CommandBus:
    def __init__(self) -> None:
        self._handlers: Dict[Type[PaymentCommand], PaymentCommand] = {}

    def register_handler(self, command_type: Type[PaymentCommand], handler: PaymentCommand) -> None:
        self._handlers[command_type] = handler

    def handle(self, command: PaymentCommand) -> str:
        handler: PaymentCommand = self._handlers[type(command)]
        return handler.execute()





if __name__ == "__main__":
    mercadoPago: PaymentCommand =  MercadoPagoPaymentCommand(amount=150.0, reference="REF123", procesor=MercadoPagoProcess())
    paypal: PaymentCommand = PaypalPaymentCommand(amount=250.0, reference="REF456", procesor=PayPalPagoProcess())

    command_bus = CommandBus()
    command_bus.register_handler(MercadoPagoPaymentCommand, mercadoPago)
    command_bus.register_handler(PaypalPaymentCommand, paypal)

    print(command_bus.handle(mercadoPago))
    print(command_bus.handle(paypal))