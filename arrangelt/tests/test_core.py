import unittest
import os
from arrangelt.core import alth_sort, ext_sort  # Import the standalone functions

class TestArrangeLT(unittest.TestCase):
    def setUp(self):
        """Set up a temporary test directory with sample files."""
        self.test_dir = "test_folder"
        os.makedirs(self.test_dir, exist_ok=True)
        
        # Create sample files
        self.files = ["a.txt", "b.txt", "c.txt", "d.csv", "e.log", "f.tmp"]
        for file in self.files:
            with open(os.path.join(self.test_dir, file), "w") as f:
                f.write("Sample content")

    def tearDown(self):
        """Clean up the test directory after tests."""
        for file in os.listdir(self.test_dir):
            os.remove(os.path.join(self.test_dir, file))
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

if __name__ == "__main__":
    unittest.main()