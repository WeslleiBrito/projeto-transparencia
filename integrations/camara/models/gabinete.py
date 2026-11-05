
from dataclasses import dataclass


@dataclass
class Gabinete:
    andar: str | None
    email: str | None
    nome: str | None
    predio: str | None
    sala: str | None
    telefone: str | None
