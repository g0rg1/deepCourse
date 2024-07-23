def merge_iterative(lst_a: list[int], lst_b: list[int]) -> list[int]:
    i = 0
    j = 0
    merged_list = []

    while i != len(lst_a) and j != len(lst_b):
        if lst_a[i] > lst_b[j]:
            merged_list.append(lst_b[j])
            j += 1
        elif lst_a[i] <= lst_b[j]:
            merged_list.append(lst_a[i])
            i += 1

    while i != len(lst_a):
        merged_list.append(lst_a[i])
        i += 1

    while j != len(lst_b):
        merged_list.append(lst_b[j])
        j += 1

    return merged_list
            

        
    


def merge_sorted(lst_a: list[int], lst_b: list[int]) -> list[int]:
    return sorted(lst_a + lst_b)

