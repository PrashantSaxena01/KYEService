from src.services.search_provider import get_search_service

_search = get_search_service()
INDEX_NAME = "fieldaid"


def search_field_data(query: str, top: int = 5) -> list[dict]:
    return _search.search(query=query, logical_index=INDEX_NAME, top=top)
