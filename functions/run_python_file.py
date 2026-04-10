import os
import config as config
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        full_wd_path = os.path.abspath(working_directory)
        full_file_path = os.path.normpath(os.path.join(full_wd_path, file_path))

        common_path = os.path.commonpath([full_wd_path, full_file_path])

        if not common_path == full_wd_path:
            raise Exception(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
        

        if not os.path.isfile(full_file_path):
            raise Exception(f'Error: "{file_path}" does not exist or is not a regular file')
        
        if not str.endswith(file_path,'.py'):
            raise Exception(f'Error: "{file_path}" is not a Python file')
        
        command = ["python", full_file_path]

        if args and len(args)>0:
            command.extend(args)

        process_run_data = subprocess.run(command, cwd=full_wd_path, capture_output=True, text=True, timeout=30)
        process_result = ''

        if process_run_data.returncode != 0:
            process_result += f"Process exited with code {process_run_data.returncode}"
        if not process_run_data.stdout and not process_run_data.stderr:
            process_result += f"No output produced"
        if process_run_data.stdout:
            process_result += f"STDOUT: {process_run_data.stdout}"
        if process_run_data.stderr:
            process_result += f"STDERR: {process_run_data.stderr}"
            

        return process_result
    
    except Exception as e:
        return f"Error: executing Python file: {e}"


