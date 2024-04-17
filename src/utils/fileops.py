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
            encoding = content[1]
            with open(file_path, 'w', encoding=encoding) as file:
                file.write(content)
        except PermissionError:
            raise PermissionError(f"Permission denied to write to the file '{filename}'.")
        except IOError as e:
            raise IOError(f"Unable to write to file '{filename}': {e}")


def read_files(directory: str) -> dict:
    """
    Recursively reads all files in the specified directory and all subdirectories,
    and returns a dictionary where each key is the filename and the value is the
    content of that file. Filenames are prefixed with their relative path for uniqueness.

    Args:
        directory (str): The path to the directory from which to read files.

    Returns:
        dict: A dictionary with filenames as keys (including their relative paths) and file contents as values.

    Raises:
        FileNotFoundError: If the specified directory does not exist.
        PermissionError: If the program lacks the necessary permissions to read the directory or files.
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"The directory '{directory}' does not exist.")
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"The path '{directory}' is not a directory.")

    files_content = {}
    for root, _, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            relative_path = os.path.relpath(file_path, start=directory)
            try:
                with open(file_path, "r", encoding="windows-1252") as file:
                    files_content[relative_path] = (file.read(), "windows-1252")
            except UnicodeDecodeError:
                with open(file_path, "r", encoding="utf-8") as file:
                    files_content[relative_path] = (file.read(), "utf-8")
            except PermissionError:
                raise PermissionError(
                    f"Permission denied to read the file '{relative_path}'."
                )
            except IOError as e:
                print(f"Unable to read file '{relative_path}': {e}")

    return files_content
