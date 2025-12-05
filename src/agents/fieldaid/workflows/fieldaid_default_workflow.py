from src.agents.base.agent_state import AgentState
from src.agents.fieldaid.fieldaid_agent import FieldAidAgent


class FieldAidDefaultWorkflow:
    def __init__(self, agent: FieldAidAgent) -> None:
        self.agent = agent

    def run(self, state: AgentState, task: str) -> dict[str, str]:
        return self.agent.run(state, task)
