from __future__ import annotations

from typing import Any

from aiphad0m.agents.base import Agent
from aiphad0m.models.events import TimelineEvent


class IdentityAgent(Agent):
    name = "identity"

    def run(self, context: dict[str, Any]) -> list[TimelineEvent]:
        duration = float(context["duration_seconds"])
        maximum = float(context["maximum_identity_intensity"])
        states = [
            ("observer", 0.00, 0.15, 0.05),
            ("aligned_participant", 0.15, 0.38, 0.25),
            ("embodied_performer", 0.38, 0.68, 0.60),
            ("distributed_performer", 0.68, 0.86, maximum),
            ("reoriented_participant", 0.86, 1.00, 0.10),
        ]
        return [
            TimelineEvent(
                start=round(duration * start, 3),
                end=round(duration * end, 3),
                kind=f"identity:{name}",
                intensity=round(min(level, maximum), 3),
                confidence=0.5,
                evidence=["explicit reversible phase-0 state model"],
            )
            for name, start, end, level in states
        ]
