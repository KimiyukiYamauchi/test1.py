import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q07 import end_up

@pytest.mark.parametrize("s, expected", [
    ("Hello", "HeLLO"),
    ("hi there", "hi thERE"),
    ("hi", "HI"),
    ("woo hoo", "woo HOO"),
    ("xyz12", "xyZ12"),
    ("x", "X"),
    ("", ""),
  
])
def test_end_up(s, expected):
    assert end_up(s) == expected
