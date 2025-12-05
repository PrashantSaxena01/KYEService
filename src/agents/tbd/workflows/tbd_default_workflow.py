from src.agents.base.agent_state import AgentState
from src.agents.tbd.tbd_agent import TBDAgent


class TBDDefaultWorkflow:
    def __init__(self, agent: TBDAgent) -> None:
        self.agent = agent

    def run(self, state: AgentState, task: str) -> dict[str, str]:
        return self.agent.run(state, task)
