from integrations.camara.client import CamaraClient

with CamaraClient() as client:

    response = client.get(
        endpoint="deputados",
        params={
            "itens": 1
        }
    )

    print(response)