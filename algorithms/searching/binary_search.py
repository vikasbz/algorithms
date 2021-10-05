from dataclasses import dataclass
from typing import List, Union

from algorithms.bucket import Bucket


@dataclass
class BinarySearch(Bucket):
    @staticmethod
    def search_recursively(values: List[int], key: int) -> Union[int, None]:
        if not values:
            print(f"Using binary search (recursive). Key: {key} not found")
            return None

        middle = len(values) // 2

        if values[middle] == key:
            print(f"Using binary search (recursive). Key: {key} found")
            return key

        elif values[middle] < key:
            return BinarySearch.search_recursively(values[middle + 1 :], key)

        else:
            return BinarySearch.search_recursively(values[:middle], key)


binary_search = BinarySearch([22, 55, 44, 11, 33, 77, 66])

if __name__ == "__main__":
    # Sort first
    binary_search.items = binary_search.using_default_sort()

    binary_search.using_default_search(55)
    binary_search.search_recursively(binary_search.items, 55)

    binary_search.using_default_search(56)
    binary_search.search_recursively(binary_search.items, 56)
