
from collections.abc import Iterator
from typing import Any

from integrations.camara.client import CamaraClient
from integrations.camara.models.deputado import Deputado
from integrations.camara.models.deputado_detalhado import DeputadoDetalhado
from integrations.camara.mappers.deputado_mapper import DeputadoMapper
from integrations.camara.mappers.deputado_detalhado_mapper import (
    DeputadoDetalhadoMapper
)
from core.pagination import iter_paginated_data


class DeputadoResource:

    def __init__(self, client: CamaraClient):
        self.client = client

    def listar(
        self,
        params: dict[str, Any] | None = None
    ) -> list[Deputado]:
        response = self.client.get(
            endpoint="deputados",
            params=params
        )

        return DeputadoMapper.from_list(response["dados"])

    def iterar_todos(
        self,
        params: dict[str, Any] | None = None
    ) -> Iterator[Deputado]:
        for data in iter_paginated_data(
            client=self.client,
            endpoint="deputados",
            params=params
        ):
            yield DeputadoMapper.from_dict(data)

    def listar_todos(
        self,
        params: dict[str, Any] | None = None
    ) -> list[Deputado]:
        return list(self.iterar_todos(params))

    def obter(self, deputado_id: int) -> DeputadoDetalhado:
        response = self.client.get(
            endpoint=f"deputados/{deputado_id}"
        )

        return DeputadoDetalhadoMapper.from_dict(response["dados"])

    def despesas(
        self,
        deputado_id: int,
        params: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        return self._get_recurso(deputado_id, "despesas", params)

    def discursos(
        self,
        deputado_id: int,
        params: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        return self._get_recurso(deputado_id, "discursos", params)

    def eventos(
        self,
        deputado_id: int,
        params: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        return self._get_recurso(deputado_id, "eventos", params)

    def frentes(self, deputado_id: int) -> dict[str, Any]:
        return self._get_recurso(deputado_id, "frentes")

    def historico(self, deputado_id: int) -> dict[str, Any]:
        return self._get_recurso(deputado_id, "historico")

    def mandatos_externos(
        self,
        deputado_id: int
    ) -> dict[str, Any]:
        return self._get_recurso(deputado_id, "mandatosExternos")

    def ocupacoes(self, deputado_id: int) -> dict[str, Any]:
        return self._get_recurso(deputado_id, "ocupacoes")

    def orgaos(
        self,
        deputado_id: int,
        params: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        return self._get_recurso(deputado_id, "orgaos", params)

    def profissoes(self, deputado_id: int) -> dict[str, Any]:
        return self._get_recurso(deputado_id, "profissoes")

    def _get_recurso(
        self,
        deputado_id: int,
        recurso: str,
        params: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        return self.client.get(
            endpoint=f"deputados/{deputado_id}/{recurso}",
            params=params
        )
