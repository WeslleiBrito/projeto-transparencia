from dataclasses import dataclass
from collections.abc import Mapping
from typing import Any

@dataclass
class Documento:
    id: int | None
    data: str | None
    fase: str | None
    autor: str | None
    codigoDocumento: str | None
    codigoDocumentoResumido: str | None
    especieTipo: str | None
    tipoEmenda: str | None

    
    @classmethod
    def from_dict(cls, dados: Mapping[str, Any]) -> "Documento":
        return cls(**dados)
