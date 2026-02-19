import os


def write_file(working_directory, file_path, content):
    full_working_directory = os.path.abspath(working_directory)
    full_file_path = os.path.normpath(os.path.join(full_working_directory, file_path))
    common_path = os.path.commonpath([full_file_path, full_working_directory])

    if not common_path == full_working_directory:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if os.path.isdir(full_file_path):
        return f'Error: Cannot write to "{file_path}" as it is a directory'
    
    os.makedirs(os.path.dirname(full_file_path), exist_ok=True)

    try:
        with open(full_file_path, 'w') as fp:
            fp.write(content)

    except Exception as e:
        return f"Error: {e}"
    
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'