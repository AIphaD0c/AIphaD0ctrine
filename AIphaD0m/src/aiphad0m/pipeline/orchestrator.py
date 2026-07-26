from __future__ import annotations

from aiphad0m.agents.dramaturgy import DramaturgyAgent
from aiphad0m.agents.identity import IdentityAgent
from aiphad0m.agents.safety import SafetyAgent
from aiphad0m.models.events import SessionPlan


class Orchestrator:
    def build(self, config: dict) -> SessionPlan:
        session = config["session"]
        context = {
            "duration_seconds": session["duration_seconds"],
            "beats": config["dramaturgy"]["beats"],
            "maximum_identity_intensity": config["identity"]["maximum_intensity"],
        }
        agents = [DramaturgyAgent(), IdentityAgent(), SafetyAgent()]
        events = []
        for agent in agents:
            events.extend(agent.run(context))
        events.sort(key=lambda event: (event.start, event.kind))
        return SessionPlan(
            title=session["title"],
            duration_seconds=float(session["duration_seconds"]),
            events=events,
            safety=config["safety"],
            identity=config["identity"],
            canon=[
                "The tool was made.",
                "The domain emerged.",
                "The signal appeared.",
                "The observations remained.",
            ],
        )
