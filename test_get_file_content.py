import functions.get_file_content as get_file_content
import config as config


def test_file_content(dir, file_path):
    try:
        results = get_file_content.get_file_content(dir, file_path)

        print(results)
        contains_truncation = f"truncated at {config.MAX_CHARS} characters" in results
        print(f"contains_truncation: {contains_truncation}")
    except Exception as e:
        print(f"{e}")
    

test_file_content("calculator", "lorem.txt")
test_file_content("calculator", "main.py")
test_file_content("calculator", "pkg/calculator.py")
test_file_content("calculator", "/bin/cat")
test_file_content("calculator", "pkg/does_not_exist.py")