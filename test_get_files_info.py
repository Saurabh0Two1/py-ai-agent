
import functions.get_files_info as file_info

def process_results(wd, d):
    results = file_info.get_files_info(wd, d)

    print(f"Result for '{"current" if d == "." else d}' directory:")
    
    if isinstance(results, list):
        for content in results:
            print(f"- {content}")
    
    else:
        print(results)


process_results("calculator", ".")
process_results("calculator", "pkg")
process_results("calculator", "/bin")
process_results("calculator", "../")


