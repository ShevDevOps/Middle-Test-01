import pytest
from typing import List
from main import diff


@pytest.fixture
def sample_data():
    """
    Provides sample data for testing.
    """
    return {
        "identical":
        (["Line 1", "Line 2", "Line 3"], ["Line 1", "Line 2", "Line 3"], []),
        "all_different":
        (["Line A", "Line B"], ["Line X", "Line Y"],
         ["Line A", "Line B", "Line X", "Line Y"]),
        "partial_overlap":
        (["Line 1", "Line 2"], ["Line 2", "Line 3"], ["Line 1", "Line 3"]),
    }


def test_diff_fixture(sample_data):
    """
    Tests the diff function using sample data.
    """
    for key, (first, second, expected) in sample_data.items():
        result = diff(first, second)
        assert result == expected


@pytest.mark.parametrize(
    "first, second, expected",
    [
        ([], ["Line 1", "Line 2"], ["Line 1", "Line 2"]),
        (["Line 1", "Line 2"], [], ["Line 1", "Line 2"]),
        ([], [], []),
        ([1, 2, 3], [2, 3], ["1"]),
        ([1, "2", 3], [2, 3], ["1"]),
    ],
)
def test_diff_param(first: List[str], second: List[str],
                    expected: List[str]) -> None:
    """
    Tests the diff function with parameterized inputs.
    """
    result = diff(first, second)
    assert result == expected
