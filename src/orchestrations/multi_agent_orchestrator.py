from src.agents.base.agent_config import AgentConfig
from src.agents.base.agent_registry import AgentRegistry
from src.agents.base.agent_state import AgentState
from src.orchestrations.routing.routing_policy import RoutingPolicy


class MultiAgentOrchestrator:
    def __init__(self, registry: AgentRegistry, routing_policy: RoutingPolicy) -> None:
        self.registry = registry
        self.routing_policy = routing_policy

    def dispatch(self, task: str, state: AgentState) -> dict[str, str]:
        agent_name = self.routing_policy.select_agent(task)
        agent = self.registry.create(agent_name, AgentConfig(name=agent_name))
        return agent.run(state, task)
