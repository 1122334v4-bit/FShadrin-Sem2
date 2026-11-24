import pytest
from app.filemanager import FileManager


@pytest.fixture
def fm(tmp_path):
    return FileManager(tmp_path)


def test_write_and_read(fm):
    fm.write_file("a.txt", "привет")
    assert fm.read_file("a.txt") == "привет"


def test_list_dir(fm):
    fm.write_file("b.txt", "1")
    fm.create_dir("folder")
    assert fm.list_dir() == ["b.txt", "folder"]


def test_copy(fm):
    fm.write_file("a.txt", "data")
    fm.copy("a.txt", "b.txt")
    assert fm.read_file("b.txt") == "data"


def test_move(fm):
    fm.write_file("a.txt", "data")
    fm.move("a.txt", "c.txt")
    assert fm.list_dir() == ["c.txt"]


def test_delete_file_and_dir(fm):
    fm.write_file("a.txt", "x")
    fm.create_dir("d")
    fm.delete("a.txt")
    fm.delete("d")
    assert fm.list_dir() == []


def test_path_traversal_blocked(fm):
    with pytest.raises(PermissionError):
        fm.read_file("../secret.txt")