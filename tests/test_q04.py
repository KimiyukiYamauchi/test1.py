import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q04 import start_hi

@pytest.mark.parametrize("s, expected", [
    ("hi there", True),
    ("hi", True),
    ("hello hi", False),
    ("he", False),
    ("h", False),
    ("", False),
    ("ho hi", False),
    ("hi ho", True),
])
def test_start_hi(s, expected):
    assert start_hi(s) == expected
