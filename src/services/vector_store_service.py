from typing import List


class VectorStoreService:
    def __init__(self) -> None:
        self._store: dict[str, list[float]] = {}

    def upsert(self, key: str, vector: list[float]) -> None:
        self._store[key] = vector

    def search(self, query: list[float], top_k: int = 3) -> List[str]:
        return list(self._store.keys())[:top_k]
