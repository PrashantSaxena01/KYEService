from src.agents.base.agent_state import AgentState
from src.orchestrations.multi_agent_orchestrator import MultiAgentOrchestrator


class TaskAssignmentWorkflow:
    def __init__(self, orchestrator: MultiAgentOrchestrator) -> None:
        self.orchestrator = orchestrator

    def run(self, task: str, state: AgentState) -> dict[str, str]:
        return self.orchestrator.dispatch(task, state)
