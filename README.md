# Chem-Tools

## Writing Tests
For each iteration of testing, create a new test suite under `tests/`. For example:
```
tests/
    test1/           <--- name of the test suite
        test1.txt    |
        test2.txt    <--- each individual test
        test3.txt    |
        ...          |
    test2/           <--- name of the test suite
        test1.txt
        test2.txt
        test3.txt
        ...
```
To create a new test suite (for example, we can name it `test3`), simply create a new directory named `test3` and add corresponding `.txt` files.
```
tests/
    test1/
        ...
    test2/
        ...
    test3/           <--- name of the test suite
        test1.txt    |
        test2.txt    <--- each individual test
        test3.txt    |
        ...          |
```