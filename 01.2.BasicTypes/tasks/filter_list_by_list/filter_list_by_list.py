def filter_list_by_list(lst_a: list[int] | range, lst_b: list[int] | range) -> list[int]:

    elements_in_b = set(lst_b)

    filtered_list = [element for element in lst_a if element not in elements_in_b]

    return filtered_list
