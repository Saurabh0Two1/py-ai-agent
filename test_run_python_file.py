
import functions.run_python_file as run_python_file

def process_results(wd, d, args=None):
    results = run_python_file.run_python_file(wd, d, args)
    print(results)


process_results("calculator", "main.py")
process_results("calculator", "main.py", ["3 + 5"])
process_results("calculator", "tests.py")
process_results("calculator", "../main.py")
process_results("calculator", "nonexistent.py")
process_results("calculator", "lorem.txt")