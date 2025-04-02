# Changelog

## [v0.3.2] - 02-04-2025
### Fixed
- Fixed detrimental error when encountering a symbolic link loop. Now skips symbolic links or directories that will cause an infinite loop. Also skips unreachable folders that throw errors.

## [v0.3.1] - 02-04-2025
### Added
- Added support for recursive file searching with a `depth` parameter for `alth_sort`, `ext_sort`, and `size_sort`.

### Changed
- Replaced `glob` with `os.scandir` for better control over file traversal.

## [v0.2.0] - 02-04-2025
### Added
- Introduced the `size_sort` function to categorize files based on their sizes.

## [v0.1.0] - 01-04-2025
### Added
- Initial release with `alth_sort` for alphabetical sorting of files.
- Added `ext_sort` for grouping files by their extensions.