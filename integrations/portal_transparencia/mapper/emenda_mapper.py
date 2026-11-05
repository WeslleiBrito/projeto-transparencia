from typing import Any

from integrations.portal_transparencia.models.emenda import Emenda

class EmendaMapper:
    
    @staticmethod
    def from_dict(data: dict[str, Any]) -> Emenda:
        return Emenda(
            codigoEmenda=data["codigoEmenda"],
            ano=data["ano"],
            tipoEmenda=data["tipoEmenda"],
            autor=data["autor"],
            nomeAutor=data["nomeAutor"],
            numeroEmenda=data["numeroEmenda"],
            localidadeDoGasto=data["localidadeDoGasto"],
            funcao=data["funcao"],
            subfuncao=data["subfuncao"],
            valorEmpenhado=data["valorEmpenhado"],
            valorLiquidado=data["valorLiquidado"],
            valorPago=data["valorPago"],
            valorRestoInscrito=data["valorRestoInscrito"],
            valorRestoCancelado=data["valorRestoCancelado"],
            valorRestoPago=data["valorRestoPago"]
            
        )
    
    @classmethod
    def from_list(
        cls,
        data: list[dict[str, Any]]
    ) -> list[Emenda]:
        return [cls.from_dict(item) for item in data]