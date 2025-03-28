import pytest 

from main import read_file

def test_read_file_not_found() -> None:
    """Checks that if the file does not exist, a FileNotFoundError is raised."""
    with pytest.raises(FileNotFoundError):
        read_file("non_existent_file.txt")
 