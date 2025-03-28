import pytest
from typing import List

from main import read_file, write_to_file


@pytest.fixture
def setup_files(tmpdir) -> tuple[str, str]:
    """
    Creates test files for verification.
    """
    testfile1 = tmpdir.join("test1.txt")
    testfile2 = tmpdir.join("test2.txt")

    testfile1.write("\n".join(["line1", "line2", "line3"]))
    testfile2.write("\n".join(["line2", "line3", "line4"]))

    return str(testfile1), str(testfile2)


def test_read_file_existing(setup_files):
    """
    Test the initial setup files.
    """
    testfile1, _ = setup_files
    lines = read_file(testfile1)
    assert lines == {"line1", "line2", "line3"}


def test_read_file_not_found() -> None:
    """
    Checks that if the file does not exist, a FileNotFoundError is raised.
    """
    with pytest.raises(FileNotFoundError):
        read_file("non_existent_file.txt")


def test_read_file_empty(tmpdir) -> None:
    """
    Test that the function `read_file` returns an empty set for an empty file.
    """
    empty_file = tmpdir.join("empty.txt")
    empty_file.write("")
    lines = read_file(str(empty_file))
    assert lines == set()


@pytest.mark.parametrize(
    "lines_to_write",
    [
        (["line1", "line2", "line3"]),
        (["apple", "banana", "cherry"]),
        ([]),
        (["line1", "line2", "line3", "line1"]),
    ],
)
def test_write_to_file_param(tmpdir, lines_to_write: List[str]) -> None:
    """Verifies writing to a file for various inputs."""
    output_file = tmpdir.join("output_param.txt")
    write_to_file(str(output_file), lines_to_write)
    with open(str(output_file), "r", encoding="utf-8") as f:
        content = f.read().splitlines()
    assert content == lines_to_write
