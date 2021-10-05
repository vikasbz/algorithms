from dataclasses import dataclass, field
from typing import List


@dataclass
class Bucket:
    items: List[int] = field(default_factory=list)

    def using_sorted(self) -> List:
        sorted_value = sorted(self.items)
        print(f"Using sorted function: {sorted_value}")
        return sorted_value


sample_bucket = Bucket([22, 55, 44, 11, 33, 77, 66])

if __name__ == "__main__":
    sample_bucket.using_sorted()
