from integrations.portal_transparencia.client import PortalTransparenciaClient
from integrations.portal_transparencia.mapper.emenda_mapper import EmendaMapper


with PortalTransparenciaClient() as client:

    response = client.get(
        endpoint="emendas",
        params={
            "ano": 2026,
            "pagina": 2,
        }
    )

    emendas = EmendaMapper.from_list(response)

    print("Conexão realizada com sucesso!")
    print(emendas[0])