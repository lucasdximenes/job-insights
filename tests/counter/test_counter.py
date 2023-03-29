from src.pre_built.counter import count_ocurrences
from unittest.mock import mock_open, patch

"""
def count_ocurrences(path: str, word: str) -> int:
    file = open(path, "r")
    read_data = file.read()
    word_count = read_data.lower().count(word.lower())
    return word_count
"""


def test_counter():
    with patch(
        "builtins.open", mock_open(read_data="Hello World!")
    ) as mock_file:
        assert count_ocurrences("path", "hello") == 1
        mock_file.assert_called_once_with("path", "r")
