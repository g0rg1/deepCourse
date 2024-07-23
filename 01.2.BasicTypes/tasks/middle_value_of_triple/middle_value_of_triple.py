def get_middle_value(a: int, b: int, c: int) -> int:
    if a <= b <= c or c <= b <= a:
        return b
    elif a <= c <= b or b <= c <= a:
        return c
    else:
        return a

