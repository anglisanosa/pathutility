# PathUtils

## Introduction
PathUtils is a utility class for handling various path-related operations in Python. It provides methods for retrieving file information, checking file existence, creating directories, detecting file encoding, and listing files in a directory.

## Installation
To install PathUtils, simply use pip:

```bash
pip install pathutils

```

## Usage Example
Here's an example of how to use the PathUtils class:

```python
from pathutils import PathUtils

# Create an instance of PathUtils
path_util = PathUtils()

# Get file information
file_path = '/path/to/file.txt'
print(f"File name: {path_util.get_filename(file_path)}")
print(f"File size: {path_util.get_file_size(file_path)} bytes")
print(f"File creation time: {path_util.get_file_creation_time(file_path)}")

# List files in a directory
directory_path = '/path/to/directory'
files_list = path_util.list_files_in_directory(directory_path)
print(f"Files in directory: {files_list}")
```

## Documentation
The Sphinx-generated documentation for PathUtils can be found [here](https://anglisanosa.github.io/pathutility/).

## Contribution
Feel free to contribute by submitting issues [here](https://github.com/anglisanosa/pathutility/issues).