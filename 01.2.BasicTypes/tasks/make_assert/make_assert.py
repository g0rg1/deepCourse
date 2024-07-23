import pytest

##############
# Code section
##############


# Don't change this function!
def ctr(clicks: int, shows: int) -> float:
    return clicks // shows if shows > 0 else 0


def ctr_correct_implementation(clicks: int, shows: int) -> float:
    assert clicks <= shows, "Clicks greater than shows"
    return clicks / shows if shows > 0 else 0.0


##############
# Test section
##############

@pytest.mark.skip
def test_check_ctr(clicks: int, shows: int, expected_result: float) -> None:
    assert ctr(clicks, shows) == expected_result, f"Wrong ctr calculation"
