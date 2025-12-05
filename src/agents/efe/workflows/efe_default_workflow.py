from src.agents.base.agent_state import AgentState
from src.agents.efe.efe_agent import EFEAgent


class EFEDefaultWorkflow:
    def __init__(self, agent: EFEAgent) -> None:
        self.agent = agent

    def run(self, state: AgentState, task: str) -> dict[str, str]:
        return self.agent.run(state, task)
