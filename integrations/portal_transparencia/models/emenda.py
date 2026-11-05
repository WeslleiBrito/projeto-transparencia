from dataclasses import dataclass
from collections.abc import Mapping
from typing import Any

@dataclass
class Emenda:
    codigoEmenda: str | None
    ano: int | None
    tipoEmenda: str | None
    autor: str | None
    nomeAutor: str | None
    numeroEmenda: str | None
    localidadeDoGasto: str | None
    funcao: str | None
    subfuncao: str | None
    valorEmpenhado: str | None
    valorLiquidado: str | None
    valorPago: str | None
    valorRestoInscrito: str | None
    valorRestoCancelado: str | None
    valorRestoPago: str | None

    @classmethod
    def from_dict(cls, dados: Mapping[str, Any]) -> "Emenda":
        return cls(**dados)
