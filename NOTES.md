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