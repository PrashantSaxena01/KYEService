from __future__ import annotations

from typing import Callable, Dict, Type

from src.agents.base.agent_config import AgentConfig
from src.agents.base.base_agent import BaseAgent


class AgentRegistry:
    """Registry for agent classes to enable dynamic creation."""

    def __init__(self) -> None:
        self._registry: Dict[str, Type[BaseAgent]] = {}

    def register(self, name: str, agent_cls: Type[BaseAgent]) -> None:
        self._registry[name] = agent_cls

    def create(self, name: str, config: AgentConfig) -> BaseAgent:
        agent_cls = self._registry.get(name)
        if not agent_cls:
            raise KeyError(f"Agent '{name}' is not registered")
        return agent_cls(config)

    def items(self) -> Dict[str, Type[BaseAgent]]:
        return dict(self._registry)
