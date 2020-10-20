import re
import os
import pytest
import inspect
import argparse
import subprocess

import session11

README_CONTENT_CHECK_FOR = ["img_resize", "jpg_to_png", "png_to_jpg"]


def test_readme_exists():
    """
    Test funtion to check if README exists.
    """
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    """
    Test if README contains atleast 200 words.
    """
    readme = open("README.md", "r", encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert (
        len(readme_words) >= 100
    ), "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    """
    Check if README contains required functions..
    """
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass

    assert (
        READMELOOKSGOOD == True
    ), "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    """
    Test function to check README file formatting.
    """
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_indentations():
    """
    Returns pass if used four spaces for each level of syntactically \
    significant indenting.
    """
    lines = inspect.getsource(session11)
    spaces = re.findall("\n +.", lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert (
            len(re.sub(r"[^ ]", "", space)) % 4 == 0
        ), "Your code indentation does not follow PEP8 guidelines"


def test_function_name_had_cap_letter():
    """
    Test function to check if any function names have any capital letters.
    """
    functions = inspect.getmembers(session11, inspect.isfunction)
    for function in functions:
        assert (
            len(re.findall("([A-Z])", function[0])) == 0
        ), "You have used Capital letter(s) in your function names"


# def test_png_to_jpg():
#     """
#     Test function for png to jpg converter.
#     """

#     lol = subprocess.run(
#         ["python", "png_to_jpg.py", "./png_images/dog10.png", "./jpg_images/"]
#     )
#     print(lol)

#     assert png_to_jpg.split(".")[-1] == "jpg"


# lol = subprocess.run(
#     ["python", "png_to_jpg.py", "./png_images/dog10.png", "./jpg_images/"]
# )
