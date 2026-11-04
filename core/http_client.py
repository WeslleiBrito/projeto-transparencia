
import time
from types import TracebackType
from typing import Any

import httpx

from core.exceptions import (
    APIConnectionError,
    APIResponseError,
    APITimeoutError
)


class HTTPClient:

    def __init__(
        self,
        base_url: str,
        timeout: float = 30.0,
        headers: dict[str, str] | None = None,
        max_retries: int = 3
    ):
        self.max_retries = max_retries

        self.client = httpx.Client(
            base_url=base_url,
            timeout=timeout,
            headers=headers
        )

    def get(
        self,
        endpoint: str,
        params: dict[str, Any] | None = None
    ) -> dict[str, Any]:

        retry_status_codes = {429, 502, 503, 504}

        for attempt in range(self.max_retries + 1):

            try:
                response = self.client.get(
                    endpoint,
                    params=params
                )

                response.raise_for_status()

                return response.json()

            except httpx.TimeoutException as error:

                if attempt == self.max_retries:
                    raise APITimeoutError(
                        "A requisição excedeu o tempo limite."
                    ) from error

            except httpx.ConnectError as error:

                if attempt == self.max_retries:
                    raise APIConnectionError(
                        "Não foi possível conectar à API."
                    ) from error

            except httpx.HTTPStatusError as error:

                status_code = error.response.status_code

                if (
                    status_code not in retry_status_codes
                    or attempt == self.max_retries
                ):
                    raise APIResponseError(
                        status_code=status_code,
                        message=error.response.text
                    ) from error

            wait_time = 2 ** attempt

            print(
                f"Falha na requisição. "
                f"Tentando novamente em {wait_time}s..."
            )

            time.sleep(wait_time)

        raise RuntimeError("Número máximo de tentativas excedido.")

    def close(self) -> None:
        self.client.close()

    def __enter__(self) -> "HTTPClient":
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None
    ) -> None:
        self.close()
