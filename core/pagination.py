
from collections.abc import Iterator
from typing import Any, TypedDict
from urllib.parse import parse_qs, urlsplit


class PaginationLink(TypedDict):
    href: str
    rel: str
    type: str


class PaginatedResponse(TypedDict):
    dados: list[dict[str, Any]]
    links: list[PaginationLink]


def iter_paginated_data(
    client: Any,
    endpoint: str,
    params: dict[str, Any] | None = None
) -> Iterator[dict[str, Any]]:

    current_params: dict[str, Any] = (params or {}).copy()

    while True:
        response: PaginatedResponse = client.get(
            endpoint=endpoint,
            params=current_params
        )

        yield from response["dados"]

        next_link: str | None = next(
            (
                link["href"]
                for link in response["links"]
                if link["rel"] == "next"
            ),
            None
        )

        if next_link is None:
            break

        query_params: dict[str, list[str]] = parse_qs(
            urlsplit(next_link).query,
            keep_blank_values=True
        )

        current_params = {
            key: values[0] if len(values) == 1 else values
            for key, values in query_params.items()
        }
