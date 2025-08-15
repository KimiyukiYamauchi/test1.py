import subprocess
import os

def run_tests_and_append_results(start=1, end=10, output_file="result.txt"):
    # すでにファイルが存在していたら削除
    if os.path.exists(output_file):
        os.remove(output_file)
        
    with open(output_file, "a", encoding="utf-8") as outfile:
        for i in range(start, end + 1):
            test_file = f"tests/test_q{i:02d}.py"
            outfile.write(f"\n=== Running {test_file} ===\n")
            try:
                result = subprocess.run(
                    ["pytest", test_file, "--tb=no", "--no-header", "--no-summary"],
                    capture_output=True,
                    text=True
                )
                outfile.write(result.stdout)
                outfile.write(result.stderr)
            except Exception as e:
                outfile.write(f"Error running {test_file}: {e}\n")

if __name__ == "__main__":
    run_tests_and_append_results()
