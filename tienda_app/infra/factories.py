import os

from .gateways import BancoNacionalProcesador


class MockPaymentProcessor:
    def pagar(
        self,
        monto: float,
        origen: str = "DESCONOCIDO",
        libro_id=None,
        stock_antes=None,
        stock_despues=None,
    ) -> bool:
        print(f"[DEBUG] Mock Payment: Procesando pago de ${monto} sin cargo real.")
        return True


class PaymentFactory:
    @staticmethod
    def get_processor():
        provider = os.getenv('PAYMENT_PROVIDER', 'BANCO')

        if provider == 'MOCK':
            return MockPaymentProcessor()

        return BancoNacionalProcesador()
