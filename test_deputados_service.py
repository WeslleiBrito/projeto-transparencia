from integrations.camara.client import CamaraClient
from integrations.camara.services.deputados_service import DeputadosService


with CamaraClient() as client:

    service = DeputadosService(client)

    # Teste 1: listar uma página
    deputados = service.listar({"itens": 5})

    print(f"Primeira consulta: {len(deputados)} deputados")

    # Teste 2: iterar por todas as páginas
    total = 0

    for deputado in service.iterar_todos({"itens": 100}):
        total += 1

        if total <= 5:
            print(deputado.nome)

    print(f"Total percorrido: {total}")

    # Teste 3: carregar todos em uma lista
    # Não execute simultaneamente com o teste anterior:
    # isso faria outra coleta completa.