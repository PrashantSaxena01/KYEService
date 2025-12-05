import os
from pathlib import Path
from typing import Any

import yaml
from dotenv import load_dotenv

load_dotenv()


class ConfigService:
    """Lightweight YAML config loader."""

    def __init__(self, base_dir: str | None = None) -> None:
        self.base_dir = Path(base_dir or os.getenv("CONFIG_DIR", "configs"))

    def load_yaml(self, name: str) -> dict[str, Any]:
        path = self.base_dir / name
        if not path.exists():
            raise FileNotFoundError(f"Config file not found: {path}")
        with path.open("r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle) or {}
            return self._expand_env(data)

    def _expand_env(self, node: Any) -> Any:
        if isinstance(node, dict):
            return {key: self._expand_env(value) for key, value in node.items()}
        if isinstance(node, list):
            return [self._expand_env(item) for item in node]
        if isinstance(node, str):
            return os.path.expandvars(node)
        return node
