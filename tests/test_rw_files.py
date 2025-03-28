import pytest 

from main import read_file 
 
@pytest.fixture
def setup_files(tmpdir) -> tuple[str, str]:
    """Creates test files for verification."""
    testfile1 = tmpdir.join("test1.txt")
    testfile2 = tmpdir.join("test2.txt")
    
    testfile1.write("\n".join(["line1", "line2", "line3"]))
    testfile2.write("\n".join(["line2", "line3", "line4"]))
    
    return str(testfile1), str(testfile2)

def test_read_file_existing(setup_files): 
    """Test the initial setup files."""
    testfile1, _ = setup_files
    lines = read_file(testfile1)
    assert lines == {"line1", "line2", "line3"}
  
def test_read_file_not_found() -> None:
    """Checks that if the file does not exist, a FileNotFoundError is raised."""
    with pytest.raises(FileNotFoundError):
        read_file("non_existent_file.txt")
 