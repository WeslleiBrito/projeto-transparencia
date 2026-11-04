from collections.abc import Iterator
from typing import Any

from integrations.camara.client import CamaraClient
from integrations.camara.models.deputado import Deputado
from integrations.camara.mappers.deputado_mapper import DeputadoMapper
from core.pagination import iter_paginated_data


class DeputadosService:

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

        return DeputadoMapper.from_list(
            response.get("dados", [])
        )

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