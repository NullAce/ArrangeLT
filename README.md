# ArrangeLT

## Overview
ArrangeLT is a Python library designed to help users quickly and efficiently sort and organize files in a directory. It provides functionality to sort files alphabetically, group files by extensions, categorize files by size, and more.

## Installation
To install the library, you can use pip. Run the following command in your terminal:

```
pip install arrangelt
```

## Usage
Here is a simple example of how to use the library:

### Sorting Files Alphabetically
```python
from arrangelt import alth_sort

# Sort files alphabetically in ascending order (default)
sorted_files = alth_sort("path/to/directory", style="asc", include_path=True)
print(sorted_files)

# Sort files alphabetically in descending order
sorted_files = alth_sort("path/to/directory", style="desc", include_path=False)
print(sorted_files)
```

### Grouping Files by Extension
```python
from arrangelt import ext_sort

# Group files by their extensions
grouped_files = ext_sort("path/to/directory", include_path=True)
print(grouped_files)

# Group files by their extensions, excluding specific types (e.g., .tmp and .log)
grouped_files = ext_sort("path/to/directory", exclude_types=[".tmp", ".log"], include_path=False)
print(grouped_files)

# Group files by their extensions, including only specific types (e.g., .txt and .csv)
grouped_files = ext_sort("path/to/directory", include_types=[".txt", ".csv"], include_path=True)
print(grouped_files)
```

### Categorizing Files by Size
```python
from arrangelt import size_sort

# Categorize files by size using default size categories
size_categories = {
    "small": (0, 10 * 1024 * 1024),   # Files smaller than 10 MB
    "medium": (10 * 1024 * 1024, 100 * 1024 * 1024),  # Files between 10 MB and 100 MB
    "large": (100 * 1024 * 1024, 1 * 1024 * 1024 * 1024),  # Files between 100 MB and 1 GB
    "extra_large": (1 * 1024 * 1024 * 1024, float('inf'))  # Files larger than 1 GB
}

categorized_files = size_sort("path/to/directory", size_categories=size_categories, include_path=True)
print(categorized_files)

# Example output:
# {
#     "small": ["path/to/directory/file1.txt"],
#     "medium": ["path/to/directory/file2.txt"],
#     "large": ["path/to/directory/file3.txt"],
#     "extra_large": ["path/to/directory/file4.txt"]
# }
```

## Features
- **Alphabetical Sorting**:
  - Sort files in ascending or descending order by their names.
  - Option to include or exclude the full file path in the output.

- **Extension Grouping**:
  - Group files by their extensions.
  - Option to include or exclude the full file path in the output.
  - Include only specific file types or exclude specific file types.

- **Size Categorization**:
  - Categorize files into size-based groups (e.g., small, medium, large).
  - Fully customizable size categories.
  - Option to include or exclude the full file path in the output.

- **Error Handling**:
  - Provides clear error messages for invalid paths, permissions, and other issues.

- **Non-File Handling**:
  - Automatically ignores non-file items (e.g., directories, symbolic links) when sorting or categorizing.

## License
This project is licensed under the Apache-2.0 License - see the LICENSE file for details.