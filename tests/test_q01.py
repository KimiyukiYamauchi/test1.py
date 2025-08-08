import sys
import os
import pytest

# src ディレクトリをインポートパスに追加（pytest.iniがない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q01 import sum_double

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (3, 2, 5),
    (2, 2, 8),
    (-1, 0, -1),
    (3, 3, 12),
    (0, 0, 0),
    (0, 1, 1),
    (3, 4, 7),
])
def test_sum_double(a, b, expected):
    assert sum_double(a, b) == expected
