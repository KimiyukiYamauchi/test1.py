import sys
import re

def count_passed_scripts(lines):
    passed_count = 0
    for line in lines:
        if line.startswith("tests/") and re.match(r"tests/test_.*\.py [.\s]+\[?\d*%?\]?$", line.strip()):
            # テスト結果部分（dotsなど）を抽出
            result_part = re.split(r"\s+", line.strip())[1]
            if 'F' not in result_part and 'E' not in result_part:
                passed_count += 1
    return passed_count

if __name__ == "__main__":
    # 標準入力から読み込む
    lines = sys.stdin.readlines()
    result = count_passed_scripts(lines)
    print(f"Passed scripts: {result}")
