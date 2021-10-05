from dataclasses import dataclass
from typing import List

from algorithms.sorting.bucket import Bucket, sample_bucket


@dataclass
class InsertionSort(Bucket):
    def sort(self) -> List:
        for i in range(1, len(self.items)):
            key = self.items[i]

            j = i - 1
            while j >= 0 and key < self.items[j]:
                self.items[j + 1] = self.items[j]
                j -= 1

            self.items[j + 1] = key

        print(f"Using insertion sort: {self.items}")
        return self.items


insertion_sort = InsertionSort(sample_bucket.items)

if __name__ == "__main__":
    insertion_sort.using_sorted()
    insertion_sort.sort()
