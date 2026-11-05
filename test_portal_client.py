
from integrations.portal_transparencia.client import PortalTransparenciaClient


with PortalTransparenciaClient() as client:

    response = client.get(
        endpoint="orgaos-siafi"
    )

    print("Conexão realizada com sucesso!")
    print(response)
