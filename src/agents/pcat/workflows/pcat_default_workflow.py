from src.agents.base.agent_state import AgentState
from src.agents.pcat.pcat_agent import PCATAgent


class PCATDefaultWorkflow:
    def __init__(self, agent: PCATAgent) -> None:
        self.agent = agent

    def run(self, state: AgentState, task: str) -> dict[str, str]:
        return self.agent.run(state, task)
