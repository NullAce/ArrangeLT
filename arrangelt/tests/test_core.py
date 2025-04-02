import unittest
import os
from arrangelt.core import alth_sort, ext_sort, size_sort  # Import the new function

def delete_setup_files(directory, files):
    """
    Delete the files created in the setUp method.

    Args:
        directory (str): The directory where the files are located.
        files (list): A list of filenames to delete.
    """
    for file in files:
        file_path = os.path.join(directory, file)
        if os.path.exists(file_path):
            os.remove(file_path)

def create_test_files(file_specs, directory):
    """
    Create test files with specified sizes.

    Args:
        file_specs (dict): A dictionary where keys are filenames and values are sizes in bytes.
        directory (str): The directory where the files will be created.
    """
    for filename, size in file_specs.items():
        file_path = os.path.join(directory, filename)
        with open(file_path, "wb") as f:
            f.write(b"a" * size)

def delete_test_files(file_specs, directory):
    """
    Delete test files created for specific tests.

    Args:
        file_specs (dict): A dictionary where keys are filenames.
        directory (str): The directory where the files are located.
    """
    for filename in file_specs.keys():
        file_path = os.path.join(directory, filename)
        if os.path.exists(file_path):
            os.remove(file_path)

class TestArrangeLT(unittest.TestCase):
    def setUp(self):
        """Set up a temporary test directory with sample files."""
        self.test_dir = os.path.join("test_folder", self._testMethodName)
        os.makedirs(self.test_dir, exist_ok=True)
        self.files = ["a.txt", "b.txt", "c.txt", "d.csv", "e.log", "f.tmp"]
        for file in self.files:
            with open(os.path.join(self.test_dir, file), "w") as f:
                f.write("Sample content")

    def tearDown(self):
        """Clean up the test directory after tests."""
        delete_setup_files(self.test_dir, self.files)
        for root, dirs, files in os.walk(self.test_dir, topdown=False):
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        os.rmdir(self.test_dir)

    def test_sort_ascending_with_path(self):
        """Test sorting in ascending order with full paths."""
        sorted_files = alth_sort(self.test_dir, "asc", include_path=True)
        expected = [os.path.join(self.test_dir, file) for file in sorted(self.files)]
        self.assertEqual(sorted_files, expected)

    def test_sort_descending_with_path(self):
        """Test sorting in descending order with full paths."""
        sorted_files = alth_sort(self.test_dir, "desc", include_path=True)
        expected = [os.path.join(self.test_dir, file) for file in sorted(self.files, reverse=True)]
        self.assertEqual(sorted_files, expected)

    def test_sort_ascending_without_path(self):
        """Test sorting in ascending order without full paths."""
        sorted_files = alth_sort(self.test_dir, "asc", include_path=False)
        expected = sorted(self.files)
        self.assertEqual(sorted_files, expected)

    def test_sort_descending_without_path(self):
        """Test sorting in descending order without full paths."""
        sorted_files = alth_sort(self.test_dir, "desc", include_path=False)
        expected = sorted(self.files, reverse=True)
        self.assertEqual(sorted_files, expected)

    def test_invalid_path(self):
        """Test handling of an invalid path."""
        with self.assertRaises(ValueError):
            alth_sort("invalid_path", "asc")

    def test_invalid_style(self):
        """Test handling of an invalid style."""
        with self.assertRaises(ValueError):
            alth_sort(self.test_dir, "invalid_style")

    def test_ext_sort_with_path(self):
        """Test grouping files by extension with full paths."""
        sorted_files = ext_sort(self.test_dir, include_path=True)
        expected = {
            '.txt': [os.path.join(self.test_dir, "a.txt"), os.path.join(self.test_dir, "b.txt"), os.path.join(self.test_dir, "c.txt")],
            '.csv': [os.path.join(self.test_dir, "d.csv")],
            '.log': [os.path.join(self.test_dir, "e.log")],
            '.tmp': [os.path.join(self.test_dir, "f.tmp")]
        }
        self.assertEqual(sorted_files, expected)

    def test_ext_sort_without_path(self):
        """Test grouping files by extension without full paths."""
        sorted_files = ext_sort(self.test_dir, include_path=False)
        expected = {
            '.txt': ["a.txt", "b.txt", "c.txt"],
            '.csv': ["d.csv"],
            '.log': ["e.log"],
            '.tmp': ["f.tmp"]
        }
        self.assertEqual(sorted_files, expected)

    def test_ext_sort_empty_directory(self):
        """Test grouping files by extension in an empty directory."""
        empty_dir = os.path.join(self.test_dir, "empty")
        os.makedirs(empty_dir, exist_ok=True)
        sorted_files = ext_sort(empty_dir, include_path=True)
        expected = {}
        self.assertEqual(sorted_files, expected)
        os.rmdir(empty_dir)

    def test_ext_sort_include_types(self):
        """Test ext_sort with include_types to include only specific extensions."""
        sorted_files = ext_sort(self.test_dir, include_types=[".txt", ".csv"], include_path=False)
        expected = {
            '.txt': ["a.txt", "b.txt", "c.txt"],
            '.csv': ["d.csv"]
        }
        self.assertEqual(sorted_files, expected)

    def test_ext_sort_exclude_types(self):
        """Test ext_sort with exclude_types to exclude specific extensions."""
        sorted_files = ext_sort(self.test_dir, exclude_types=[".log", ".tmp"], include_path=False)
        expected = {
            '.txt': ["a.txt", "b.txt", "c.txt"],
            '.csv': ["d.csv"]
        }
        self.assertEqual(sorted_files, expected)

    def test_ext_sort_include_and_exclude_types(self):
        """Test ext_sort with both include_types and exclude_types."""
        sorted_files = ext_sort(self.test_dir, include_types=[".txt", ".csv", ".log"], exclude_types=[".log"], include_path=False)
        expected = {
            '.txt': ["a.txt", "b.txt", "c.txt"],
            '.csv': ["d.csv"]
        }
        self.assertEqual(sorted_files, expected)

    def test_size_sort_default_categories(self):
        """Test size_sort with default size categories."""
        # Remove files created in setUp
        delete_setup_files(self.test_dir, self.files)

        # Create files of different sizes
        file_specs = {
            "small.txt": 5 * 1024 * 1024,  # 5 MB
            "medium.txt": 15 * 1024 * 1024,  # 15 MB
            "large.txt": 150 * 1024 * 1024,  # 150 MB
            "extra_large.txt": 2 * 1024 * 1024 * 1024  # 2 GB
        }

        try:
            create_test_files(file_specs, self.test_dir)
            sorted_files = size_sort(self.test_dir, include_path=False)
            expected = {
                "small": ["small.txt"],
                "medium": ["medium.txt"],
                "large": ["large.txt"],
                "extra_large": ["extra_large.txt"]
            }
            self.assertEqual(sorted_files, expected)
        finally:
            delete_test_files(file_specs, self.test_dir)

    def test_size_sort_custom_categories(self):
        """Test size_sort with custom size categories."""
        # Remove files created in setUp
        delete_setup_files(self.test_dir, self.files)

        custom_categories = {
            "tiny": (0, 1 * 1024 * 1024),  # Files smaller than 1 MB
            "small": (1 * 1024 * 1024, 10 * 1024 * 1024),  # Files between 1 MB and 10 MB
            "big": (10 * 1024 * 1024, float('inf'))  # Files larger than 10 MB
        }

        file_specs = {
            "tiny.txt": 512 * 1024,  # 512 KB
            "small.txt": 5 * 1024 * 1024,  # 5 MB
            "big.txt": 20 * 1024 * 1024  # 20 MB
        }

        try:
            create_test_files(file_specs, self.test_dir)
            sorted_files = size_sort(self.test_dir, size_categories=custom_categories, include_path=False)
            expected = {
                "tiny": ["tiny.txt"],
                "small": ["small.txt"],
                "big": ["big.txt"]
            }
            self.assertEqual(sorted_files, expected)
        finally:
            delete_test_files(file_specs, self.test_dir)

    def test_size_sort_empty_directory(self):
        """Test size_sort in an empty directory."""
        # Remove files created in setUp
        delete_setup_files(self.test_dir, self.files)

        empty_dir = os.path.join(self.test_dir, "empty")
        os.makedirs(empty_dir, exist_ok=True)
        try:
            sorted_files = size_sort(empty_dir, include_path=True)
            expected = {}  # Expect an empty dictionary
            self.assertEqual(sorted_files, expected)
        finally:
            os.rmdir(empty_dir)  # Ensure the directory is removed

    def test_size_sort_invalid_categories(self):
        """Test size_sort with invalid size categories."""
        invalid_categories = {
            "invalid": (10, 5)  # Invalid: max_size is less than min_size
        }
        with self.assertRaises(ValueError):
            size_sort(self.test_dir, size_categories=invalid_categories)

    def test_size_sort_include_path(self):
        """Test size_sort with include_path=True."""
        # Remove files created in setUp
        delete_setup_files(self.test_dir, self.files)

        file_specs = {
            "small.txt": 5 * 1024 * 1024  # 5 MB
        }

        try:
            create_test_files(file_specs, self.test_dir)
            sorted_files = size_sort(self.test_dir, include_path=True)
            expected = {
                "small": [os.path.join(self.test_dir, "small.txt")],
                "medium": [],
                "large": [],
                "extra_large": []
            }
            self.assertEqual(sorted_files, expected)
        finally:
            delete_test_files(file_specs, self.test_dir)

if __name__ == "__main__":
    unittest.main()