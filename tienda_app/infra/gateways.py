import datetime
from typing import Optional

from ..domain.interfaces import ProcesadorPago

class BancoNacionalProcesador(ProcesadorPago):
    """
    Implementación concreta de la infraestructura.
    Simula un banco local escribiendo en un log.
    """
    def pagar(
        self,
        monto: float,
        origen: str = "DESCONOCIDO",
        libro_id: Optional[int] = None,
        stock_antes: Optional[int] = None,
        stock_despues: Optional[int] = None,
    ) -> bool:
        # Simulamos una operación de red o persistencia externa
        archivo_log = "pagos_locales_Emmanuel_Alvarez_Castrilon.log"
        with open(archivo_log, "a") as f:
            f.write(
                f"ORIGEN: {origen} | Libro ID: {libro_id} | "
                f"Stock antes: {stock_antes}\n"
            )
            f.write(f"[{datetime.datetime.now()}] BANCO NACIONAL - Cobro procesado: ${monto}\n")
            f.write(
                f"Libro ID: {libro_id} | "
                f"Stock despues de la compra: {stock_despues}\n"
            )
        return True