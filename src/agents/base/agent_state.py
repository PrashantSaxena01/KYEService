from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class AgentState:
    conversation_id: str
    history: List[str] = field(default_factory=list)
    context: Dict[str, Any] = field(default_factory=dict)
