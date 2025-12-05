from src.agents.base.agent_state import AgentState
from src.agents.ims.ims_agent import IMSAgent


class IMSDefaultWorkflow:
    def __init__(self, agent: IMSAgent) -> None:
        self.agent = agent

    def run(self, state: AgentState, task: str) -> dict[str, str]:
        return self.agent.run(state, task)
