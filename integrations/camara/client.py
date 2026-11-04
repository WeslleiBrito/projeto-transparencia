
from types import TracebackType
from typing import Any

from core.http_client import HTTPClient


class CamaraClient:

    BASE_URL = "https://dadosabertos.camara.leg.br/api/v2"

    def __init__(
        self,
        timeout: float = 30.0,
        max_retries: int = 3
    ):
        self.http = HTTPClient(
            base_url=self.BASE_URL,
            timeout=timeout,
            max_retries=max_retries,
            headers={
                "Accept": "application/json"
            }
        )

    def get(
        self,
        endpoint: str,
        params: dict[str, Any] | None = None
    ) -> dict[str, Any]:

        return self.http.get(
            endpoint=endpoint,
            params=params
        )

    def close(self) -> None:
        self.http.close()

    def __enter__(self) -> "CamaraClient":
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None
    ) -> None:
        self.close()
