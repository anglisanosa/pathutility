       
import os
import chardet
from path_utils.utils.errors import FileOperationError

class PathUtils:
    """
    A utility class for handling path-related operations.

    Attributes:
        properties (dict): A dictionary containing properties retrieved based on the provided parameters.
    """

    
    @staticmethod
    def get_parent_directory(path):
        """
        Get the parent directory of a given path.

        Args:
            path (str): The path from which to get the parent directory.

        Returns:
            str: The parent directory path.
        """
        return os.path.dirname(path)

    @staticmethod
    def get_filename(path):
        """
        Get the filename from a path.

        Args:
            path (str): The path from which to extract the filename.

        Returns:
            str: The filename.
        """
        return os.path.basename(path)

    @staticmethod
    def get_file_extension(path):
        """
        Get the file extension from a path.

        Args:
            path (str): The path from which to extract the extension.

        Returns:
            str: The file extension.
        """
        return os.path.splitext(path)[1]

    @staticmethod
    def get_filename_without_extension(path):
        """
        Get the filename without its extension from a path.

        Args:
            path (str): The path from which to extract the filename.

        Returns:
            str: The filename without extension.
        """
        return os.path.splitext(os.path.basename(path))[0]

    @staticmethod
    def get_file_size(path):
        """
        Get the size of a file in bytes.

        Args:
            path (str): The path to the file.

        Returns:
            int: The size of the file in bytes.
        """
        return os.path.getsize(path)

    @staticmethod
    def get_file_creation_time(path):
        """
        Get the creation time of a file.

        Args:
            path (str): The path to the file.

        Returns:
            float: The creation time of the file.
        """
        return os.path.getctime(path)

    @staticmethod
    def get_file_modification_time(path):
        """
        Get the last modification time of a file.

        Args:
            path (str): The path to the file.

        Returns:
            float: The last modification time of the file.
        """
        return os.path.getmtime(path)

    @staticmethod
    def get_file_access_time(path):
        """
        Get the last access time of a file.

        Args:
            path (str): The path to the file.

        Returns:
            float: The last access time of the file.
        """
        return os.path.getatime(path)

    @staticmethod
    def is_file_exists(path):
        """
        Check if a file exists.

        Args:
            path (str): The path to the file.

        Returns:
            bool: True if the file exists, False otherwise.
        """
        return os.path.exists(path)

    @staticmethod
    def create_directory_if_not_exists(path):
        """
        Create a directory if it doesn't exist.

        Args:
            path (str): The path to the directory to be created.
        """
        if not os.path.exists(path):
            os.makedirs(path)

    @staticmethod
    def get_file_encoding(path):
        """
        Detect file encoding.

        Args:
            path (str): The path to the file.

        Returns:
            str or None: The detected encoding or None if an error occurs.
        """
        try:
            with open(path, 'rb') as f:
                encoding = chardet.detect(f.read())['encoding']
                return encoding
        except Exception as e:
            raise FileOperationError(f"Error detecting file encoding: {e}")
        
    @staticmethod
    def list_files_in_directory(directory):
        """
        List all files in a directory.

        Args:
            directory (str): The path to the directory.

        Returns:
            list: A list of filenames in the directory.
        """
        try:
            return [file for file in os.listdir(directory) if os.path.isfile(os.path.join(directory, file))]
        except Exception as e:
            raise FileOperationError(f"Error listing files in directory: {e}")
        

