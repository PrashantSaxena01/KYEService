from typing import List

from src.agents.base.agent_state import AgentState
from src.orchestrations.multi_agent_orchestrator import MultiAgentOrchestrator


class CrossAgentWorkflow:
    def __init__(self, orchestrator: MultiAgentOrchestrator) -> None:
        self.orchestrator = orchestrator

    def run(self, tasks: List[str], state: AgentState) -> list[dict[str, str]]:
        return [self.orchestrator.dispatch(task, state) for task in tasks]
