def reverse_iterative(lst: list[int]) -> list[int]:
    reversed_list = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list


def reverse_inplace_iterative(lst: list[int]) -> None:
    for i in range(len(lst) // 2):
        lst[i], lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]



def reverse_inplace(lst: list[int]) -> None:
    lst.reverse()


def reverse_reversed(lst: list[int]) -> list[int]:
    return list(reversed(lst))


def reverse_slice(lst: list[int]) -> list[int]:
    return lst[::-1]
