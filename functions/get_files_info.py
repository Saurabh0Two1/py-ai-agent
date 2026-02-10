import os


def get_files_info(working_directory, directory="."):
    try:
        full_working_directory_path = os.path.abspath(working_directory)
        normalized_target_directory_path = os.path.normpath(os.path.join(full_working_directory_path, directory))

        # check if its a directory to proceed
        if not os.path.isdir(normalized_target_directory_path):
            raise Exception(f'Error: "{directory}" is not a directory')

        # check if the target directory is strictly within the working directory
        common_path = os.path.commonpath([normalized_target_directory_path, full_working_directory_path])

        if not common_path == full_working_directory_path:
            raise Exception(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')

        contentsList = []

        get_dir_contents(contentsList, normalized_target_directory_path)

        return contentsList
    
    except Exception as e:
        return f"{e}"


def get_dir_contents(contentsList, target_directory_path):
    for file_name in os.listdir(target_directory_path):
        full_path = os.path.join(target_directory_path, file_name)
        if os.path.isfile(full_path):
            contentsList.append(f"{file_name}: file_size={os.path.getsize(full_path)} bytes, is_dir={False}")
        else:
            contentsList.append(f"{file_name}: file_size={os.path.getsize(full_path)} bytes, is_dir={True}")
            get_dir_contents(contentsList, full_path) 


    



    