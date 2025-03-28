import pytest
from typing import List
from main import same

@pytest.mark.parametrize("lines1, lines2, result", [
    ([],[],[]),
    (["line"],[],[]),
    ([],["line"],[]),
    (["line"],["line"],["line"]),
    (["line1"],["line2"],[]),
    (["line1", "line2"],["line1", "line3"],["line1"])
])
def test_same(lines1 : List[str], lines2 : List[str], result : List[str]):
    assert same(lines1, lines2) == result