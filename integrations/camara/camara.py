
from types import TracebackType

from integrations.camara.client import CamaraClient
from integrations.camara.resources.deputado import DeputadoResource


class Camara:

    def __init__(
        self,
        timeout: float = 30.0,
        max_retries: int = 3
    ):
        self.client = CamaraClient(
            timeout=timeout,
            max_retries=max_retries
        )

        self.deputado = DeputadoResource(
            client=self.client
        )

    def close(self) -> None:
        self.client.close()

    def __enter__(self) -> "Camara":
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None
    ) -> None:
        self.close()
