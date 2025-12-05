from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from src.agents.base.agent_config import AgentConfig
from src.agents.base.agent_state import AgentState


class BaseAgent(ABC):
    """Abstract agent interface."""

    def __init__(self, config: AgentConfig) -> None:
        self.config = config

    @property
    def name(self) -> str:
        return self.config.name

    @abstractmethod
    def run(self, state: AgentState, task: str) -> Any:
        """Execute the agent for a given task and state."""
        raise NotImplementedError
