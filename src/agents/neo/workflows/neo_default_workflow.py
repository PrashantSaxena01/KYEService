from src.agents.base.agent_state import AgentState
from src.agents.neo.neo_agent import NEOAgent


class NEODefaultWorkflow:
    def __init__(self, agent: NEOAgent) -> None:
        self.agent = agent

    def run(self, state: AgentState, task: str) -> dict[str, str]:
        return self.agent.run(state, task)
