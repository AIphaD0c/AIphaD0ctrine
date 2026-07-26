from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from aiphad0m.models.events import TimelineEvent


class Agent(ABC):
    name: str

    @abstractmethod
    def run(self, context: dict[str, Any]) -> list[TimelineEvent]:
        """Return structured, timestamped observations or cues."""
        raise NotImplementedError
