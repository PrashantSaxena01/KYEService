from typing import Any, Dict, List, Optional

from azure.core.credentials import AzureKeyCredential
from azure.identity import DefaultAzureCredential
from azure.search.documents import SearchClient


class AzureAISearchService:
    """Thin wrapper around Azure AI Search clients with per-index caching."""

    def __init__(self, endpoint: str, api_key: Optional[str] = None, index_map: Optional[Dict[str, str]] = None) -> None:
        self.endpoint = endpoint.rstrip("/")
        self.index_map = index_map or {}
        if api_key:
            self.credential = AzureKeyCredential(api_key)
        else:
            self.credential = DefaultAzureCredential()
        self._clients: Dict[str, SearchClient] = {}

    def _resolve_index(self, logical_index: str) -> str:
        return self.index_map.get(logical_index, logical_index)

    def _get_client(self, logical_index: str) -> SearchClient:
        index_name = self._resolve_index(logical_index)
        if index_name not in self._clients:
            self._clients[index_name] = SearchClient(endpoint=self.endpoint, index_name=index_name, credential=self.credential)
        return self._clients[index_name]

    def search(self, query: str, logical_index: str, top: int = 5) -> List[Dict[str, Any]]:
        client = self._get_client(logical_index)
        results = client.search(search_text=query, top=top)
        return [self._format_result(doc) for doc in results]

    def _format_result(self, doc: Any) -> Dict[str, Any]:  # type: ignore[no-any-unimported]
        data = dict(doc)
        data.setdefault("score", getattr(doc, "@search.score", None))
        return data
