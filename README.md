# Session 11

This is the readme for session-11.
This file contains information for functions present in `session11.py` and `test_session11.py`.

## Run Tests

```
pytest -v
```

## Functions in `session11.py`.

The function definitions are as follows:

### get_input_args()

    parser.add_argument("op", type=str, help="Choose op type.")

### calc_percent_change(w: int, h: int, p: int) -> "New H/W":

    Calculate new height and width based on percent change.

### img_resize(input_img_path: str, output_img_path: str, \*\*kwargs) -> "Resized Image":

    Function to resize image based on parameters provided.
    Percent based, height based, width based.

### jpg2png(read_img_path: str, save_img_path: str) -> "png image":

    Function to convert a jpeg image to png.

### png2jpg(read_img_path: str, save_img_path: str) -> "jpg image":

    Function to convert a png image to jpg.

## Functions in `test_session11.py`.

The test definitions are as follows:

### test_readme_exists()

    Test funtion to check if README exists.

### test_readme_contents()

    Test if README contains atleast 200 words.

### test_readme_proper_description()

    Check if README contains required functions..

### test_readme_file_for_formatting()

    Test function to check README file formatting.

### test_indentations()

    Returns pass if used four spaces for each level of syntactically \

### test_function_name_had_cap_letter()

    Test function to check if any function names have any capital letters.
