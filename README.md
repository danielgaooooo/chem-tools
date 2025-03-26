# Chem-Tools

## Step 1: Install Required Dependencies
* Make sure you have Python3 installed.
* Download [git](https://git-scm.com/downloads).

## Step 2: Navigate to Proper Directory
* Open Git Bash
* Navigate to where you've put the `main.py` script.
    * For example, if `main.py` is on your `Desktop`:
        ```
        cd ~/Desktop
        ```
        will take you to your Desktop.
        ```
        ls
        ```
        should confirm that `main.py` is present.
    * For me, since my `main.py` lives at `~/Documents/dev/chem_code`, it looks like this:
        ```
        > cd ~/Documents/dev/chem_code 
        > ls
        README.md       data.txt     main.py
        ```
## Step 3: Run Program
Once you are in the proper directory, run:
```
python3 main.py data.txt
```
where `data.txt` is your input data. You can name your data file whatever you 
want, just tell the script where to find it. For example, if your data file is 
at `~/Downloads/data/weights.txt`, run instead:
```
python3 main.py ~/Downloads/data/weights.txt
```

## Formatting Your Data
The program expects your data file to be formatted in a certain way. That 
format is:
```
SUM
ERROR
LIST OF NUMBERS
```
where `SUM` is a number, `ERROR` is a number between 0 and 1, and `LIST OF NUMBERS` 
represents the weights that could add up to `SUM`. An example of a valid data 
file is:
```
10
0.01
1 2 3 4 5 6 7 8 9 10
```
where the desired sum is 10, within a 1% error, with possible weights of 1, 2, 
3, 4, 5, 6, 7, 8, 9, and 10.