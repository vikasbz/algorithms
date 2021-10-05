from dataclasses import dataclass, field
from typing import List, Union


@dataclass
class Bucket:
    items: List[int] = field(default_factory=list)

    def using_default_sort(self) -> List[int]:
        sorted_value = sorted(self.items)

        print(f"Using sorted function: {sorted_value}")
        return sorted_value

    def using_default_search(self, key: int) -> Union[int, None]:
        if key in self.items:
            print(f"Key: {key} found")
            return key

        print(f"Key: {key} not found")
        return None


sample_bucket = Bucket([22, 55, 44, 11, 33, 77, 66])

if __name__ == "__main__":
    # Sorting
    sample_bucket.using_default_sort()

    # Search
    _ = sample_bucket.using_default_search(key=55)
    _ = sample_bucket.using_default_search(key=56)
