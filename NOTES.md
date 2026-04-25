# NOTES

## Testing `tests.py` locally

In terminal:
```
pytest tests.py -v
```

Also, remove `--headless` from your options:
```
options.add_argument("--headless")  # comment this line out
```

The output after running `pytest tests.py -v` should be:
```
=============================================================== test session starts ================================================================
platform win32 -- Python 3.12.9, pytest-9.0.3, pluggy-1.6.0 -- C:\Users\Li-Ting\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Li-Ting\Documents\Projects\QA-Automation-Showcase
collected 0 items
=============================================================== no tests ran in 0.19s ==============================================================
```

`collected 0 items` means pytest found your file, read it successfully, found no errors, and found zero test functions. That is correct because you have not written any tests yet.

After adding the pytest fixture and the login helper function, add TC01.

After adding TC01, run `pytest tests.py -v`.

It outputs:
```
================================================================ test session starts =================================================================
platform win32 -- Python 3.12.9, pytest-9.0.3, pluggy-1.6.0 -- C:\Users\Li-Ting\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Li-Ting\Documents\Projects\QA-Automation-Showcase
collected 1 item                                                                                                                                      

tests.py::test_valid_login PASSED                                                                                                               [100%]

================================================================= 1 passed in 37.67s =================================================================
```

To run a specific test function in `tests.py`, run this instead i.e. Add `::function_name` after the file name:
```
pytest tests.py::test_invalid_login -v
```

Now the second test should pass:
```
=============================================================== test session starts ================================================================
platform win32 -- Python 3.12.9, pytest-9.0.3, pluggy-1.6.0 -- C:\Users\Li-Ting\AppData\Local\Programs\Python\Python312\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\Li-Ting\Documents\Projects\QA-Automation-Showcase
collected 2 items                                                                                                                                   

tests.py::test_valid_login PASSED                                                                                                             [ 50%]
tests.py::test_invalid_login PASSED                                                                                                           [100%]

================================================================ 2 passed in 23.59s ================================================================
```


## Creating a `.gitignore` file

The `tests.cpython-312-pytest-9....` file is a pytest cache file. Python compiles your `.py` file into bytecode when it runs, and pytest saves some metadata alongside it.