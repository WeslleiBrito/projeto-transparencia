from integrations.camara import Camara

with Camara() as camara:

    deputado = camara.deputado.obter(204379)

    despesas = camara.deputado.despesas(
        deputado_id=204379,
        params={
            "ano": 2026,
            "itens": 10
        }
    )

    print("Deputado:", deputado.nomeCivil, "idLegislatura:", deputado.ultimoStatus.idLegislatura)

    print("\nResposta completa das despesas:")
    print(despesas)

    print("\nDados:")
    print(despesas.get("dados"))