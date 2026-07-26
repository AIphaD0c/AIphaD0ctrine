from __future__ import annotations

from typing import Any

from aiphad0m.agents.base import Agent
from aiphad0m.models.events import TimelineEvent


class DramaturgyAgent(Agent):
    name = "dramaturgy"

    def run(self, context: dict[str, Any]) -> list[TimelineEvent]:
        duration = float(context["duration_seconds"])
        beats = context["beats"]
        weights = [0.12, 0.10, 0.20, 0.12, 0.20, 0.14, 0.12]
        cursor = 0.0
        events: list[TimelineEvent] = []
        for index, beat in enumerate(beats):
            span = duration * weights[index % len(weights)]
            end = duration if index == len(beats) - 1 else min(duration, cursor + span)
            intensity = min(1.0, 0.18 + index * 0.13)
            if beat in {"release", "afterimage"}:
                intensity *= 0.55
            events.append(
                TimelineEvent(
                    start=round(cursor, 3),
                    end=round(end, 3),
                    kind=f"dramaturgy:{beat}",
                    intensity=round(intensity, 3),
                    confidence=0.5,
                    evidence=["synthetic phase-0 plan"],
                )
            )
            cursor = end
        return events
