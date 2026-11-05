
from dataclasses import dataclass

from integrations.camara.models.ultimo_status import UltimoStatus


@dataclass
class DeputadoDetalhado:
    cpf: str | None
    dataFalecimento: str | None
    dataNascimento: str | None
    escolaridade: str | None
    id: int
    municipioNascimento: str | None
    nomeCivil: str | None
    redeSocial: list[str]
    sexo: str | None
    ufNascimento: str | None
    ultimoStatus: UltimoStatus
    uri: str
    urlWebsite: str | None
