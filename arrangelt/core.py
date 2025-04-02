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
        files = [file for file in files if os.path.isfile(file)]
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
        if not os.path.isfile(file):  # Ensure it's a file
            continue

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


def size_sort(path: str, size_categories: dict = None, include_path: bool = True) -> dict:
    """
    Categorize files in a directory based on their sizes.

    Args:
        path (str): The absolute directory path containing the files.
        size_categories (dict): A dictionary defining size categories. Defaults to predefined categories.
            Example:
            {
                "small": (0, 10 * 1024 * 1024),   # Files smaller than 10 MB
                "medium": (10 * 1024 * 1024, 100 * 1024 * 1024),  # Files between 10 MB and 100 MB
                "large": (100 * 1024 * 1024, 1 * 1024 * 1024 * 1024),  # Files between 100 MB and 1 GB
                "extra_large": (1 * 1024 * 1024 * 1024, float('inf'))  # Files larger than 1 GB
            }
        include_path (bool): Whether to include the full path in the output. Defaults to True.

    Returns:
        dict: A dictionary where keys are size categories and values are lists of file paths or filenames.

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

    # Default size categories if none are provided
    if size_categories is None:
        size_categories = {
            "small": (0, 10 * 1024 * 1024),   # Files smaller than 10 MB
            "medium": (10 * 1024 * 1024, 100 * 1024 * 1024),  # Files between 10 MB and 100 MB
            "large": (100 * 1024 * 1024, 1 * 1024 * 1024 * 1024),  # Files between 100 MB and 1 GB
            "extra_large": (1 * 1024 * 1024 * 1024, float('inf'))  # Files larger than 1 GB
        }
    else:
        # Validate the size_categories dictionary
        if not isinstance(size_categories, dict):
            raise TypeError("The 'size_categories' argument must be a dictionary.")
        for category, size_range in size_categories.items():
            if not isinstance(category, str):
                raise ValueError(f"Invalid category name '{category}'. All keys must be strings.")
            if not (isinstance(size_range, tuple) and len(size_range) == 2):
                raise ValueError(f"Invalid size range for category '{category}'. Each value must be a tuple of two elements.")
            min_size, max_size = size_range
            if not (isinstance(min_size, (int, float)) and isinstance(max_size, (int, float))):
                raise ValueError(f"Invalid size range for category '{category}'. Both elements must be numbers.")
            if min_size < 0:
                raise ValueError(f"Invalid size range for category '{category}'. Minimum size must be non-negative.")
            if max_size < min_size:
                raise ValueError(f"Invalid size range for category '{category}'. Maximum size must be greater than or equal to the minimum size.")

    try:
        files = glob.glob(os.path.join(path, '*'))
    except PermissionError:
        raise PermissionError(f"Permission denied for accessing the directory '{path}'.")

    if not files:
        print(f"No files found in the directory '{path}'.")
        return {}

    size_dict = {category: [] for category in size_categories}

    for file in files:
        if os.path.isfile(file):  # Ensure it's a file
            file_size = os.path.getsize(file)
            for category, (min_size, max_size) in size_categories.items():
                if min_size <= file_size < max_size:
                    size_dict[category].append(file if include_path else os.path.basename(file))
                    break

    return size_dict