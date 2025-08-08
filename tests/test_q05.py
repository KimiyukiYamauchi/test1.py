import sys
import os
import pytest

# src ディレクトリをパスに追加（pytest.ini がない場合）
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from q05 import del_del

@pytest.mark.parametrize("s, expected", [
    ("adelbc", "abc"),
    ("adelHello", "aHello"),
    ("adedbc", "adedbc"),
    ("abcdel", "abcdel"),
    ("add", "add"),
    ("ad", "ad"),
    ("a", "a"),
    ("", ""),
    ("del", "del"),
    ("adel", "a"),
    ("aadelbb", "aadelbb"),
])
def test_del_del(s, expected):
    assert del_del(s) == expected
