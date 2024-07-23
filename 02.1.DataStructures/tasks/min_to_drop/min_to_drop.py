import typing as tp


def get_min_to_drop(seq: tp.Sequence[tp.Any]) -> int:
    if len(seq) < 2:
        return 0

    unique_elements = set(seq)
    max_count = 0
    for element in unique_elements:
        count = seq.count(element)
        max_count = max(max_count, count)

    return len(seq) - max_count
