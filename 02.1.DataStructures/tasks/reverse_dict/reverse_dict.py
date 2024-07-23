import typing as tp


def revert(dct: tp.Mapping[str, str]) -> dict[str, list[str]]:
    reversed_dict = {}
    for key, value in dct.items():
        reversed_dict.setdefault(value, []).append(key)
    return reversed_dict
