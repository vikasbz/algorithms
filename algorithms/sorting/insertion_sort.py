from dataclasses import dataclass
from typing import List

from algorithms.sorting.bucket import Bucket


@dataclass
class InsertionSort(Bucket):
    def sort(self) -> List[int]:
        for index, key in enumerate(self.items[1:]):
            while index >= 0 and key < self.items[index]:
                self.items[index + 1] = self.items[index]
                index -= 1
            self.items[index + 1] = key

        print(f"Using insertion sort: {self.items}")
        return self.items


insertion_sort = InsertionSort([22, 55, 44, 11, 33, 77, 66])

if __name__ == "__main__":
    insertion_sort.using_sorted()
    insertion_sort.sort()
