import sys
import os
import pytest

# src ディレクトリをインポートパスに追加（pytest.iniがない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q03 import front3

@pytest.mark.parametrize("s, expected", [
    ("Java", "JavJavJav"),
    ("Chocolate", "ChoChoCho"),
    ("abc", "abcabcabc"),
    ("abcXYZ", "abcabcabc"),
    ("ab", "ababab"),
    ("a", "aaa"),
    ("", ""),
])
def test_front3(s, expected):
    assert front3(s) == expected
