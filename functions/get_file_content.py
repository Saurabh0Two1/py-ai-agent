import os
import config as config

def get_file_content(working_directory, file_path):
    full_working_directory = os.path.abspath(working_directory)
    full_file_path = os.path.normpath(os.path.join(full_working_directory, file_path))

    common_path = os.path.commonpath([full_working_directory, full_file_path])

    if not common_path == full_working_directory:
        raise Exception(f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')
    
    if not os.path.isfile:
        raise Exception(f'Error: File not found or is not a regular file: "{file_path}"')

    try:
        with open(full_file_path, "r") as f:
            content = f.read(config.MAX_CHARS)

            if f.read(1):
                content += f'[...File "{file_path}" truncated at {config.MAX_CHARS} characters]'
    
    except Exception as e:
        raise Exception(f"error: {e}")
    
    return content
    


    
    
