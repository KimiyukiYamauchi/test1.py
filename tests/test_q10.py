import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q10
 import array123

@pytest.mark.parametrize("nums, expected", [
    ([1, 1, 2, 3, 1], True),
    ([1, 1, 2, 4, 1], False),
    ([1, 1, 2, 1, 2, 3], True),
    ([1, 2, 1, 2, 1], False),
    ([1, 2, 3, 1, 2, 3], True),
    ([1, 2, 3], True),
    ([1, 1, 1], False),
    ([1, 2], False),
    ([1], False),
    ([], False),
])
def test_array123(nums, expected):
    assert array123(nums) == expected
