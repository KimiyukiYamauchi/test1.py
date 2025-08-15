import re
import sys

def count_passed_scripts_from_file(file_path):
    passed_count = 0

    with open(file_path, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # テストファイル行にマッチ (例: tests/test_q01.py ........)
            match = re.match(r"^(tests/test_.*\.py)\s+([.FE]+)", line)
            if match:
                result_str = match.group(2)
                if 'F' not in result_str and 'E' not in result_str:
                    passed_count += 1

    return passed_count

if __name__ == "__main__":
    # 標準入力から読み込む
    lines = sys.stdin.readlines()
    result = count_passed_scripts(lines)
    print(f"Passed scripts: {result}")
