from dataclasses import dataclass


@dataclass
class Deputado:

    email: str | None
    id: int
    idLegislatura: int
    nome: str
    siglaPartido: str | None
    siglaUf: str
    uri: str
    uriPartido: str | None
    urlFoto: str