
from types import TracebackType
from typing import Any

from config.settings import settings
from core.http_client import HTTPClient


class PortalTransparenciaClient:

    BASE_URL = "https://api.portaldatransparencia.gov.br/api-de-dados"

    def __init__(
        self,
        timeout: float = 30.0,
        max_retries: int = 3
    ):
        if settings.PORTAL_API_KEY is None:
            raise ValueError(
                "A chave da API do Portal da Transparência não foi configurada."
            )

        self.http = HTTPClient(
            base_url=self.BASE_URL,
            timeout=timeout,
            max_retries=max_retries,
            headers={
                "Accept": "application/json",
                "chave-api-dados": settings.PORTAL_API_KEY.get_secret_value()
            }
        )

    def get(
        self,
        endpoint: str,
        params: dict[str, Any] | None = None
    ) -> list[dict[str, Any]]:

        return self.http.get(
            endpoint=endpoint,
            params=params
        )

    def close(self) -> None:
        self.http.close()

    def __enter__(self) -> "PortalTransparenciaClient":
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None
    ) -> None:
        self.close()
