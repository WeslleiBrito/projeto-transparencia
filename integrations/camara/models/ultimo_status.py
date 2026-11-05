
from dataclasses import dataclass

from integrations.camara.models.gabinete import Gabinete


@dataclass
class UltimoStatus:
    condicaoEleitoral: str | None
    data: str | None
    descricaoStatus: str | None
    email: str | None
    gabinete: Gabinete | None
    id: int
    idLegislatura: int
    nome: str
    nomeEleitoral: str | None
    siglaPartido: str | None
    siglaUf: str
    situacao: str | None
    uri: str
    uriPartido: str | None
    urlFoto: str | None
