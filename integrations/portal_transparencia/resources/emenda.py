from collections.abc import Iterator
from typing import Any

from integrations.portal_transparencia.client import PortalTransparenciaClient
from integrations.portal_transparencia.models.emenda import Emenda
from integrations.portal_transparencia.mapper.emenda_mapper import EmendaMapper
from core.pagination import iter_paginated_data


class EmendaResource:
    
    def __init__(self, client: PortalTransparenciaClient) -> None:
        self.client = client
    
    