def get_squares(elements: list[int]) -> list[int]:
    sorted_list = []
    for element in elements:
        element = element**2
        sorted_list.append(element)
    return sorted_list




# ====================================================================================================


def get_indices_from_one(elements: list[int]) -> list[int]:
    return list(range(1 , len(elements) + 1))




# ====================================================================================================


def get_max_element_index(elements: list[int]) -> int | None:
    if not elements:
        return None
    
    max_element_index = 0
    for i in range(1, len(elements)):
        if elements[i] > elements[max_element_index]:
            max_element_index = i
    
    return max_element_index


# ====================================================================================================


def get_every_second_element(elements: list[int]) -> list[int]:
    return elements[1::2]


# ====================================================================================================


def get_first_three_index(elements: list[int]) -> int | None:
    for i, element in enumerate(elements):
        if element == 3:
            return i
    return None


# ====================================================================================================


def get_last_three_index(elements: list[int]) -> int | None:
    for i in range(len(elements) - 1, -1, -1):
        if elements[i] == 3:
            return i
    return None


# ====================================================================================================


def get_sum(elements: list[int]) -> int:
    sum = 0
    for element in elements:
        sum+= element
    return sum


# ====================================================================================================


def get_min_max(elements: list[int], default: int | None) -> tuple[int | None, int | None]:
    if not elements:
        return default, default
    
    min_element = elements[0]
    max_element = elements[0]
    for element in elements:
        if element < min_element:
            min_element = element
        if element > max_element:
            max_element = element
    
    return min_element, max_element


# ====================================================================================================


def get_by_index(elements: list[int], i: int, boundary: int) -> int | None:
    if i < 0 or i >= len(elements):
        return None
    if elements[i] > boundary:
        return elements[i]
    return None
