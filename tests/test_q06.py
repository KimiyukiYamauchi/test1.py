import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q06 import max1020

@pytest.mark.parametrize("a, b, expected", [
    (11, 19, 19),
    (19, 11, 19),
    (11, 9, 11),
    (9, 21, 0),
    (10, 21, 10),
    (21, 10, 10),
    (9, 11, 11),
    (23, 10, 10),
    (20, 10, 20),
    (7, 20, 20),
    (17, 16, 17),
    (10, 20, 20),
    (20, 10, 20),
    (10, 10, 10),
    (15, 25, 15),
    (25, 15, 15),
    (30, 40, 0),
])
def test_max1020(a, b, expected):
    assert max1020(a, b) == expected
