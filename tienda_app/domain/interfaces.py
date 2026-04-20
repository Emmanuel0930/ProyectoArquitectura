from abc import ABC, abstractmethod
from typing import Optional

class ProcesadorPago(ABC):
    """
    D: Inversión de Dependencias.
    Definimos el CONTRATO que cualquier banco debe seguir.
    """
    @abstractmethod
    def pagar(
        self,
        monto: float,
        origen: str = "DESCONOCIDO",
        libro_id: Optional[int] = None,
        stock_antes: Optional[int] = None,
        stock_despues: Optional[int] = None,
    ) -> bool:
        pass