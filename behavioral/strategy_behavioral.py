"""
Ejemplos de uso: El patrón Adapter es muy común en el código Python. Se utiliza muy a menudo en sistemas basados en algún código heredado. 
En estos casos, los adaptadores crean código heredado con clases modernas.

Identificación: Adapter es reconocible por un constructor que toma una instancia de distinto tipo de clase abstracta/interfaz. 
Cuando el adaptador recibe una llamada a uno de sus métodos, convierte los parámetros 
al formato adecuado y después dirige la llamada a uno o varios métodos del objeto envuelto.

https://refactoring.guru/es/design-patterns/adapter/python/example


"""

from abc import ABC, abstractmethod
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        ...

    @abstractmethod
    def refund(self, amount: float) -> str:
        ...


class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Paid {amount} using Credit Card."

    def refund(self, amount: float) -> str:
        return f"Refunded {amount} to Credit Card."


class PaypalPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Paid {amount} using PayPal."

    def refund(self, amount: float) -> str:
        return f"Refunded {amount} to PayPal."


class PaymentFacade:
    def __init__(self, strategy: PaymentStrategy) -> None:
        self.strategy = strategy

    def make_payment(self, amount: float) -> str:
        return self.strategy.pay(amount)

    def make_refund(self, amount: float) -> str:
        return self.strategy.refund(amount)


if __name__ == "__main__":
    credit_card_payment: PaymentStrategy = CreditCardPayment()
    paypal_payment: PaymentStrategy = PaypalPayment()

    payment_facade_cc = PaymentFacade(strategy=credit_card_payment)
    print(payment_facade_cc.make_payment(100.0))
    print(payment_facade_cc.make_refund(50.0))

    payment_facade_pp = PaymentFacade(strategy=paypal_payment)
    print(payment_facade_pp.make_payment(200.0))
    print(payment_facade_pp.make_refund(75.0))