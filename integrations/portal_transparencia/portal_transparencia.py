from types import TracebackType

from integrations.portal_transparencia.client import PortalTransparenciaClient
from integrations.portal_transparencia.resources.emenda import EmendaResource

class PortalTransparencia:

    def __init__(
        self,
        timeout: float = 30.0,
        max_retries: int = 3
    ):
        self.client = PortalTransparenciaClient(
            timeout=timeout,
            max_retries=max_retries
        )

        self.emenda = EmendaResource(
            client=self.client
        )

    def close(self) -> None:
        self.client.close()

    def __enter__(self) -> "PortalTransparencia":
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None
    ) -> None:
        self.close()