from __future__ import annotations

from typing import Any

from aiphad0m.agents.base import Agent
from aiphad0m.models.events import TimelineEvent


class SafetyAgent(Agent):
    name = "safety"

    def run(self, context: dict[str, Any]) -> list[TimelineEvent]:
        duration = float(context["duration_seconds"])
        return [
            TimelineEvent(
                start=0.0,
                end=duration,
                kind="safety:immediate_exit_available",
                intensity=1.0,
                confidence=1.0,
                evidence=["configuration requirement"],
            ),
            TimelineEvent(
                start=max(0.0, duration - 30.0),
                end=duration,
                kind="safety:reorientation",
                intensity=1.0,
                confidence=1.0,
                evidence=["post-session reorientation enabled"],
            ),
        ]
