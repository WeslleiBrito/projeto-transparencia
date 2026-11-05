from typing import Any

from integrations.portal_transparencia.models.orgao_siafi import OrgaoSiafi


class OrgaoSiafiMapper:

    @staticmethod
    def from_dict(data: dict[str, Any]) -> OrgaoSiafi:
        return OrgaoSiafi(
            codigo=data["codigo"],
            descricao=data["descricao"]
        )

    @classmethod
    def from_list(
        cls,
        data: list[dict[str, Any]]
    ) -> list[OrgaoSiafi]:
        return [cls.from_dict(item) for item in data]