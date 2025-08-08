import sys
import os
import pytest

# src ディレクトリをインポートパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q08 import front_times

@pytest.mark.parametrize("s, n, expected", [
    ("Chocolate", 2, "ChoCho"),
    ("Chocolate", 3, "ChoChoCho"),
    ("Abc", 3, "AbcAbcAbc"),
    ("Ab", 4, "AbAbAbAb"),
    ("A", 4, "AAAA"),
    ("", 4, ""),
    ("Abc", 0, ""),
])
def test_front_times(s, n, expected):
    assert front_times(s, n) == expected
