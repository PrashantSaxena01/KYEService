class RoutingPolicy:
    def __init__(self) -> None:
        self.keyword_map = {
            "catalog": "pcat",
            "inventory": "ims",
            "field": "fieldaid",
            "efe": "efe",
            "neo": "neo",
        }

    def select_agent(self, task: str) -> str:
        lowered = task.lower()
        for keyword, agent in self.keyword_map.items():
            if keyword in lowered:
                return agent
        return "tbd"
