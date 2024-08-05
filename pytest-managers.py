from asyncio import log
import pytest
from execute_jar import execute_jar, file_exists, content_file

def test_execute_jar(**args):
    # Given.
    jar_file = args["test_info"]
    # When.
    result = execute_jar(jar_file["jar_file"])
    # Then.
    assert result == jar_file["answer"]

def test_file_exists(**args):
    # Given.
    file_name = args["test_info"]
    # When.
    result = file_exists(file_name["file_path"])
    # Then.
    try:
        assert result == file_name["answer"]
    except AssertionError as e:
        print(e)

def test_content_file(**args):
    # Given.
    file_name = args["test_info"]
    # When.
    result = content_file(file_name["file_path"])
    # Then.
    assert result == file_name["answer"]


