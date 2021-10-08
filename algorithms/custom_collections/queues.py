from dataclasses import dataclass, field
from typing import Any


@dataclass
class Queue:
    items: list = field(default_factory=list)

    def put(self, value: Any):
        self.items.insert(0, value)

    def get(self):
        return self.items.pop()

    @property
    def size(self) -> int:
        return len(self.items)


if __name__ == "__main__":
    q = Queue()

    print(q.size)

    q.put(11)
    q.put("Aa")
    q.put(22)
    q.put(33)
    q.put("Bb")

    print(q.items)

    print(q.get())
    print(q.get())
    print(q.items)
