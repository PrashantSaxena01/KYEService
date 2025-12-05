from functools import lru_cache

from src.services.azure_ai_search_service import AzureAISearchService
from src.services.config_service import ConfigService


@lru_cache(maxsize=1)
def get_search_service() -> AzureAISearchService:
    settings = ConfigService().load_yaml("settings.yaml")
    search_settings = settings.get("services", {}).get("azure_ai_search", {})
    endpoint = search_settings.get("endpoint")
    api_key = search_settings.get("api_key")
    indexes = search_settings.get("indexes", {})
    return AzureAISearchService(endpoint=endpoint, api_key=api_key, index_map=indexes)
