from src.agents.base.agent_state import AgentState
from src.orchestrations.routing.routing_policy import RoutingPolicy


class Router:
    def __init__(self, policy: RoutingPolicy) -> None:
        self.policy = policy

    def route(self, task: str, state: AgentState) -> str:
        return self.policy.select_agent(task)
