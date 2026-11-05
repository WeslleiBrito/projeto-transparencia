
from typing import Any

from integrations.camara.models.deputado_detalhado import DeputadoDetalhado
from integrations.camara.models.ultimo_status import UltimoStatus
from integrations.camara.models.gabinete import Gabinete


class DeputadoDetalhadoMapper:

    @staticmethod
    def _mapear_gabinete(
        data: dict[str, Any] | None
    ) -> Gabinete | None:

        if data is None:
            return None

        return Gabinete(
            andar=data.get("andar"),
            email=data.get("email"),
            nome=data.get("nome"),
            predio=data.get("predio"),
            sala=data.get("sala"),
            telefone=data.get("telefone")
        )

    @classmethod
    def _mapear_ultimo_status(
        cls,
        data: dict[str, Any]
    ) -> UltimoStatus:

        return UltimoStatus(
            condicaoEleitoral=data.get("condicaoEleitoral"),
            data=data.get("data"),
            descricaoStatus=data.get("descricaoStatus"),
            email=data.get("email"),
            gabinete=cls._mapear_gabinete(data.get("gabinete")),
            id=data["id"],
            idLegislatura=data["idLegislatura"],
            nome=data["nome"],
            nomeEleitoral=data.get("nomeEleitoral"),
            siglaPartido=data.get("siglaPartido"),
            siglaUf=data["siglaUf"],
            situacao=data.get("situacao"),
            uri=data["uri"],
            uriPartido=data.get("uriPartido"),
            urlFoto=data.get("urlFoto")
        )

    @classmethod
    def from_dict(
        cls,
        data: dict[str, Any]
    ) -> DeputadoDetalhado:

        return DeputadoDetalhado(
            cpf=data.get("cpf"),
            dataFalecimento=data.get("dataFalecimento"),
            dataNascimento=data.get("dataNascimento"),
            escolaridade=data.get("escolaridade"),
            id=data["id"],
            municipioNascimento=data.get("municipioNascimento"),
            nomeCivil=data.get("nomeCivil"),
            redeSocial=data.get("redeSocial", []),
            sexo=data.get("sexo"),
            ufNascimento=data.get("ufNascimento"),
            ultimoStatus=cls._mapear_ultimo_status(
                data["ultimoStatus"]
            ),
            uri=data["uri"],
            urlWebsite=data.get("urlWebsite")
        )
