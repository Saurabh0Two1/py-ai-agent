from functions.write_file import write_file

def execute_test_case(working_directory, file_path, content):
    results = write_file(working_directory, file_path, content)
    print(results)



execute_test_case("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
execute_test_case("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
execute_test_case("calculator", "/tmp/temp.txt", "this should not be allowed")
