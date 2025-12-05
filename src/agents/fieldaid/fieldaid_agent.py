from src.agents.base.base_agent import BaseAgent
from src.agents.base.agent_state import AgentState


class FieldAidAgent(BaseAgent):
    def run(self, state: AgentState, task: str) -> dict[str, str]:
        state.history.append(task)
        return {"agent": self.name, "task": task, "result": f"{self.name} handled {task}"}
