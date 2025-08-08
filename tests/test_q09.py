import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q09 import last2

@pytest.mark.parametrize("s, expected", [
    ("hixxhi", 1),
    ("xaxxaxaxx", 1),
    ("axxxaaxx", 2),
    ("xxaxxaxxaxx", 3),
    ("xaxaxaxx", 0),
    ("xxxx", 2),
    ("13121312", 1),
    ("11212", 1),
    ("13121311", 0),
    ("1717171", 2),
    ("hi", 0),
    ("h", 0),
    ("", 0),
])
def test_last2(s, expected):
    assert last2(s) == expected
