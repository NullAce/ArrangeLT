# ArrangeLT

## Overview
ArrangeLT is a Python library designed to help users quickly and efficiently sort and organize files in a directory. It provides functionality to sort files alphabetically, group files by extensions, and more. ArrangeLT is lightweight, easy to use, and highly extensible.

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

## Features
- **Alphabetical Sorting**:
  - Sort files in ascending or descending order by their names.
  - Option to include or exclude the full file path in the output.

- **Extension Grouping**:
  - Group files by their extensions.
  - Option to include or exclude the full file path in the output.
  - Include only specific file types or exclude specific file types.

- **Error Handling**:
  - Provides clear error messages for invalid paths, permissions, and other issues.

## License
This project is licensed under the Apache-2.0 License - see the LICENSE file for details.