from collections.abc import Iterator
from typing import Any

from integrations.portal_transparencia.client import PortalTransparenciaClient
from integrations.portal_transparencia.models.emenda import Emenda
from integrations.portal_transparencia.mapper.emenda_mapper import EmendaMapper
from integrations.portal_transparencia.models.documento import Documento
from integrations.portal_transparencia.mapper.documento_mapper import DocumentoMapper
from core.pagination import iter_paginated_data


class EmendaResource:
    
    def __init__(self, client: PortalTransparenciaClient) -> None:
        self.client = client
    

    def listar(
        self,
        params: dict[str, Any] | None = None
    ) -> list[Emenda]:
        response = self.client.get(
            endpoint="emendas",
            params=params
        )

        return EmendaMapper.from_list(response)


    def iterar_todos(
        self,
        params: dict[str, Any] | None = None
    ) -> Iterator[Emenda]:
        for data in iter_paginated_data(
            client=self.client,
            endpoint="emendas",
            params=params
        ):
            yield EmendaMapper.from_dict(data)

    
    def obter_documento(self, codigo_emenda: str) -> list[Documento]:
        response = self.client.get(
            endpoint=f"emendas/documentos/{codigo_emenda}"
        )

        return DocumentoMapper.from_list(response)