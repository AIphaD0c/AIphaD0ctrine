from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any


@dataclass(slots=True)
class TimelineEvent:
    start: float
    end: float
    kind: str
    intensity: float
    confidence: float = 1.0
    evidence: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class SessionPlan:
    title: str
    duration_seconds: float
    events: list[TimelineEvent]
    safety: dict[str, Any]
    identity: dict[str, Any]
    canon: list[str]

    def to_dict(self) -> dict[str, Any]:
        return {
            "title": self.title,
            "duration_seconds": self.duration_seconds,
            "events": [event.to_dict() for event in self.events],
            "safety": self.safety,
            "identity": self.identity,
            "canon": self.canon,
        }
