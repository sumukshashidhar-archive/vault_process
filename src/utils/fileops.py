import os

def write_files(files_content: dict, directory: str) -> None:
    """
    Writes contents to files based on a dictionary mapping from filenames to contents. Files
    will be created or overwritten in the specified directory.

    Args:
        files_content (dict): A dictionary where each key is a filename and each value is the content to write to that file.
        directory (str): The directory in which to write the files.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        PermissionError: If the program lacks the necessary permissions to write to the directory or files.
        IOError: If there is an issue writing to the files.
    """
    if not os.path.exists(directory):
        os.makedirs(directory)  # Creates the directory if it does not exist
    elif not os.path.isdir(directory):
        raise NotADirectoryError(f"The path '{directory}' is not a directory.")

    for filename, content in files_content.items():
        file_path = os.path.join(directory, filename)
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
        except PermissionError:
            raise PermissionError(f"Permission denied to write to the file '{filename}'.")
        except IOError as e:
            raise IOError(f"Unable to write to file '{filename}': {e}")


def read_files(directory: str) -> dict:
    """
    Reads all files in the specified directory and returns a dictionary where each
    key is the filename and the value is the content of that file.

    Args:
        directory (str): The path to the directory from which to read files.

    Returns:
        dict: A dictionary with filenames as keys and file contents as values.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        PermissionError: If the program lacks the necessary permissions to read the directory or files.
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"The path '{directory}' is not a directory.")

    files_content = {}
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    files_content[filename] = file.read()
            except PermissionError:
                raise PermissionError(
                    f"Permission denied to read the file '{filename}'."
                )
            except IOError as e:
                print(f"Unable to read file '{filename}': {e}")

    return files_content
