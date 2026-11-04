

class Deputado:
    def __init__(
            self,
            email: str,
            id: int,
            idLegislatura: int,
            nome: str,
            siglaPartido: str,
            siglaUf: str,
            uri: str,
            uriPartido: str,
            urlFoto: str
        ):
        self.email = email
        self.id = id
        self.idLegislatura = idLegislatura
        self.nome = nome
        self.siglaPartido = siglaPartido
        self.siglaUf = siglaUf
        self.uri = uri
        self.uriPartido = uriPartido
        self.urlFoto = urlFoto
