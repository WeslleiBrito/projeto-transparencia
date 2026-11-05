
from integrations.camara.client import CamaraClient
from integrations.camara.mappers.deputado_detalhado_mapper import (
    DeputadoDetalhadoMapper
)


deputado_id = 204379

with CamaraClient() as client:

    response = client.get(
        endpoint=f"deputados/{deputado_id}"
    )

    deputado = DeputadoDetalhadoMapper.from_dict(
        response["dados"]
    )

    print("Nome civil:", deputado.nomeCivil)
    print("Nascimento:", deputado.dataNascimento)
    print("Escolaridade:", deputado.escolaridade)
    print("Partido:", deputado.ultimoStatus.siglaPartido)
    print("Gabinete:", deputado.ultimoStatus.gabinete)
