import os
import glob

def alth_sort(path: str, style: str = "asc", include_path: bool = True) -> list:
    """
    Sort files in a directory alphabetically in ascending or descending order.

    Args:
        path (str): The absolute directory path containing the files.
        style (str): Sorting style ('asc' for ascending, 'desc' for descending). Defaults to 'asc'.
        include_path (bool): Whether to include the full path in the output. Defaults to True.

    Returns:
        list: A sorted list of file paths or filenames.

    Note:
        This function does not recursively check subfolders for files. It only processes files
        in the specified directory.
    """
    if not isinstance(path, str):
        raise TypeError("The 'path' argument must be a string.")
    if not os.path.exists(path):
        raise ValueError(f"The path '{path}' does not exist.")
    if not os.path.isdir(path):
        raise ValueError(f"The path '{path}' is not a directory.")

    valid_styles = ['asc', 'desc']
    if style not in valid_styles:
        raise ValueError(f"Invalid style '{style}'. Valid options are: {valid_styles}")

    try:
        files = glob.glob(os.path.join(path, '*'))
    except PermissionError:
        raise PermissionError(f"Permission denied for accessing the directory '{path}'.")

    if not files:
        print(f"No files found in the directory '{path}'.")
        return []

    if style == 'asc':
        sorted_files = sorted(files, key=lambda x: os.path.basename(x))
    elif style == 'desc':
        sorted_files = sorted(files, key=lambda x: os.path.basename(x), reverse=True)

    if not include_path:
        return [os.path.basename(file) for file in sorted_files]

    return sorted_files


def ext_sort(path: str, include_path: bool = True, include_types: list = None, exclude_types: list = None) -> dict:
    """
    Group files in a directory by their extensions.

    Args:
        path (str): The absolute directory path containing the files.
        include_path (bool): Whether to include the full path in the output. Defaults to True.
        include_types (list): A list of file extensions to include (e.g., ['.txt', '.csv']). Defaults to None.
        exclude_types (list): A list of file extensions to exclude (e.g., ['.tmp', '.log']). Defaults to None.

    Returns:
        dict: A dictionary where keys are file extensions and values are lists of file paths or filenames.

    Note:
        This function does not recursively check subfolders for files. It only processes files
        in the specified directory.
    """
    if not isinstance(path, str):
        raise TypeError("The 'path' argument must be a string.")
    if not os.path.exists(path):
        raise ValueError(f"The path '{path}' does not exist.")
    if not os.path.isdir(path):
        raise ValueError(f"The path '{path}' is not a directory.")

    try:
        files = glob.glob(os.path.join(path, '*'))
    except PermissionError:
        raise PermissionError(f"Permission denied for accessing the directory '{path}'.")

    if not files:
        print(f"No files found in the directory '{path}'.")
        return {}

    ext_dict = {}
    for file in files:
        _, ext = os.path.splitext(file)
        ext = ext.lower() if ext else "no_extension"

        # Include only files with extensions in include_types (if specified)
        if include_types and ext not in include_types:
            continue

        # Skip files with extensions in exclude_types (if specified)
        if exclude_types and ext in exclude_types:
            continue

        if ext not in ext_dict:
            ext_dict[ext] = []
        ext_dict[ext].append(file if include_path else os.path.basename(file))

    return ext_dict