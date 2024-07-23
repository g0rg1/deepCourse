import typing as tp
import heapq


def merge(seq: tp.Sequence[tp.Sequence[int]]) -> list[int]:
    heap = [(list[0], i, 0) for i, list in enumerate(seq) if list]
    heapq.heapify(heap)

    merged_list = []

    while heap:
        val, list_index, element_index = heapq.heappop(heap)
        merged_list.append(val)

        if element_index + 1 < len(seq[list_index]):
            heapq.heappush(heap, (seq[list_index][element_index + 1], list_index, element_index + 1))

    return merged_list