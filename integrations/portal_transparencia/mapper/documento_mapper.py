from typing import Any

from integrations.portal_transparencia.models.documento import Documento

class DocumentoMapper:
    
    @staticmethod
    def from_dict(data: dict[str, Any]) -> Documento:
        return Documento(
            id=data.get("id"),
            data=data.get("data"),
            fase=data.get("fase"),
            autor=data.get("autor"),
            codigoDocumento=data.get("codigoDocumento"),
            codigoDocumentoResumido=data.get("codigoDocumentoResumido"),
            especieTipo=data.get("especieTipo"),
            tipoEmenda=data.get("tipoEmenda")
        )

    
    @classmethod
    def from_list(
        cls,
        data: list[dict[str, Any]]
    ) -> list[Documento]:
        return [cls.from_dict(item) for item in data]