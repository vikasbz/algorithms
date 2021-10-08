from dataclasses import dataclass, field
from typing import Any


@dataclass
class Queue:
    items: list = field(default_factory=list)

    def put(self, value: Any):
        self.items.insert(0, value)

    def get(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
