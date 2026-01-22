

"""
Abstract Factory es un patrón de diseño creacional que nos permite producir familias de objetos relacionados sin especificar sus clases concretas.

El patrón Abstract Factory define una interfaz para crear todos los productos, pero deja la propia creación de productos 
para las clases de fábrica concretas. Cada tipo de fábrica se corresponde con cierta variedad de producto.

https://refactoring.guru/es/design-patterns/abstract-factory/python/example

"""

from abc import ABC, abstractmethod
from datetime import datetime

class Payment(ABC):
    

    @abstractmethod
    def pay(self, amount:float, reference:str) -> str:
        ...
    
    @abstractmethod
    def get_information_pay_by_id(self, pay_id:int) -> str:
        ...
    
    @abstractmethod
    def get_history_by_reference_pay(self, reference:str) -> str:
        ...




class MercadoPagoPayment(Payment):

    def pay(self, amount:float, reference:str) -> str:
        return f"Se pago en MercadoPago - cantidad: {amount} -  a la referencia: {reference}"
    
    
    def get_information_pay_by_id(self, pay_id:int) -> str:
        return f"El pago con al referencia:MERCA123 -> se realizo enl dia: {datetime.now().isoformat()}"
        
    
    def get_history_by_reference_pay(self, reference:str) -> str:
        return f"Hisotira de la referencia: {reference} - movimeintos 10 en las ultamas 24 horas"


class PayPalPaymet(Payment):

    def pay(self, amount:float, reference:str) -> str:
        return f"Se pago en Paypal - cantidad: {amount} -  a la referencia: {reference}"
    
    
    def get_information_pay_by_id(self, pay_id:int) -> str:
        return f"El pago con al referencia:PAYOAL123 -> se realizo enl dia: {datetime.now().isoformat()}"
        
    
    def get_history_by_reference_pay(self, reference:str) -> str:
        return f"Hisotira de la referencia: {reference} - movimeintos 10 en las ultamas 24 horas"



        
def pay_account_imp(pago:Payment, amount:float, reference:str) -> None:

    print(pago.pay(amount=amount, reference=reference))
    print(pago.get_information_pay_by_id(pay_id=123))
    print(pago.get_history_by_reference_pay(reference=reference))


        

if __name__ == "__main__":

    mercado: Payment = MercadoPagoPayment()

    print("Procesando pago en Mercado Pago")
    pay_account_imp(pago=mercado, amount=150.34, reference="mercado12334")

    paypal: Payment = PayPalPaymet()

    print("Procesando pago en Paypal")
    pay_account_imp(pago=paypal, amount=7781.34, reference="paypal2124")



