from integrations.camara.models.deputado import Deputado
from typing import Any

class DeputadoMapper:

    @staticmethod
    def from_dict(data: dict[str, Any]) -> Deputado:

        return Deputado(
            email=data.get("email"),
            id=data["id"],
            idLegislatura=data["idLegislatura"],
            nome=data["nome"],
            siglaPartido=data.get("siglaPartido"),
            siglaUf=data["siglaUf"],
            uri=data["uri"],
            uriPartido=data.get("uriPartido"),
            urlFoto=data["urlFoto"]
        )

    @classmethod
    def from_list(cls, data: list[dict[str, Any]]) -> list[Deputado]:

        return [
            cls.from_dict(item)
            for item in data
        ]