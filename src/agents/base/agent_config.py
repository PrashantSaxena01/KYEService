from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class AgentConfig:
    name: str
    description: str = ""
    tools: List[str] = field(default_factory=list)
    workflows: List[str] = field(default_factory=list)
    parameters: Dict[str, Any] = field(default_factory=dict)
