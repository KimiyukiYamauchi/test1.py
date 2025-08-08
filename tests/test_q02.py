import sys
import os
import pytest

# src ディレクトリをインポートパスに追加（pytest.iniがない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q02 import near_hundred

@pytest.mark.parametrize("n, expected", [
    (93, True),
    (90, True),
    (89, False),
    (110, True),
    (111, False),
    (121, False),
    (-101, False),
    (-209, False),
    (190, True),
    (209, True),
    (0, False),
    (5, False),
    (-50, False),
    (191, True),
    (189, False),
    (200, True),
    (210, True),
    (211, False),
    (290, False),
])
def test_near_hundred(n, expected):
    assert near_hundred(n) == expected
